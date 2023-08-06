"""Plugin for accounts that should sum up to zero. Determines transactions
that when taken together, sum up to zero, and move them to a specified
account. The remaining entries are the 'unmatched' ones, that need attention
from the user.

Motivation:
-----------

Real-world transfers frequently occur between accounts. For example, between a
checking account and an investment account. When double entry bookkeeping is
used to track such transfers, we end up with two problems:

    a) when account statements are converted to double-entry format, the user
    has to manually match the transfers on account statements from the two
    institutions involved, and remove one of the entries since they are
    redundant.

    b) even when (a) is done, the transfer might take a day or more to
    complete: the two accounts involved would then reflect the transfer on
    different dates.

Since the money is truly missing from all the physical accounts for the period
of transfer, they can be accounted for as shown in this example:

2005-01-01 Transfer
  Assets:Bank_of_Ameriplus  -20 USD
  ZeroSumAccount:Transfers

2005-01-03 Transfer
  Assets:TB_Trading  20 USD
  ZeroSumAccount:Transfers

Doing so has a few advantages:

    a) on 2005-01-02, your assets are accurately represented:
    Bank_of_Ameriplus is short by $20, TB_Trading still doesn't have it, and
    the ZeroSumAccount:Transfers account captures that the money is still
    yours, but is "in flight."

    b) One can convert each bank's transactions directly into double-entry
    ledger statements. No need to remove the transaction from one of the
    banks. When you look at your journal files for each account, they match
    your account statements exactly.

    c) Import/conversion (from say, a bank .csv or .ofx) is easier, because
    your import scripts don't have to figure out where a transfer goes, and
    can simply assign transfers to  ZeroSumAccount:Transfers

    d) If there is a problem, your ZeroSumAccount:Transfers will sum to a
    non-zero value. Errors can therefore be found easily.


What this plugin does:
----------------------

Account statements from institutions can be directly converted to double-entry
format, with transfers simply going to a special transfers account (eg:
Assets:ZeroSumAccount:Transfers).

In this plugin, we identify sets of postings in the specified ZeroSum accounts
that sum up to zero, and move them to a specified target account. This target
account will always sum up to zero and needs no further attention. The
postings remaining in the original ZeroSum accounts were the ones that could
not be matched, and potentially need attention.

The plugin operates on postings (not transactions) in the ZeroSum accounts.
This way, transactions with multiple postings to a ZeroSum account are still
matched without special handling.

The following examples will be matched and moved by this plugin:

    Example 1:
    ----------
    Input:
        2005-01-01 Transfer
          Assets:Bank_of_Ameriplus  -20 USD
          ZeroSumAccount:Transfers

        2005-01-03 Transfer
          Assets:TB_Trading  20 USD
          ZeroSumAccount:Transfers
    Output:
        2005-01-01 Transfer
          Assets:Bank_of_Ameriplus  -20 USD
          ZeroSumAccount-Matched:Transfers

        2005-01-03 Transfer
          Assets:TB_Trading  20 USD
          ZeroSumAccount-Matched:Transfers

    Example 2 (Only input shown):
    -----------------------------
    2005-01-01 Transfer
      Assets:Bank_of_Ameriplus  -20 USD
      ZeroSumAccount:Transfers   10 USD
      ZeroSumAccount:Transfers   10 USD

    2005-01-03 Transfer
      Assets:TB_Trading_A  10 USD
      ZeroSumAccount:Transfers

    2005-01-04 Transfer
      Assets:TB_Trading_B  10 USD
      ZeroSumAccount:Transfers

The following examples will NOT be matched:

    Example A:
    ----------
    2005-01-01 Transfer
      Assets:Bank_of_Ameriplus  -20 USD
      ZeroSumAccount:Transfers   10 USD
      ZeroSumAccount:Transfers   10 USD

    2005-01-03 Transfer
      Assets:TB_Trading  20 USD
      ZeroSumAccount:Transfers

    Example B:
    ----------
    2005-01-01 Transfer
      Assets:Bank_of_Ameriplus  -20 USD
      ZeroSumAccount:Transfers

    2005-01-03 Transfer
      Assets:TB_Trading_A  10 USD
      ZeroSumAccount:Transfers

    2005-01-03 Transfer
      Assets:TB_Trading_B  10 USD
      ZeroSumAccount:Transfers


The plugin does not append/remove the original set of input transaction
entries. It only changes the accounts to which postings are made. The plugin
also automatically adds "Open" directives for the target accounts to which
matched transactions are moved.

Invoking the plugin:
--------------------
First, an example:

    plugin "beancount.plugins.zerosum" "{
     'zerosum_accounts' : {
     'Assets:Zero-Sum-Accounts:Bank-Account-Transfers' : ('Assets:ZSA-Matched:Bank-Account-Transfers', 30),
     'Assets:Zero-Sum-Accounts:Credit-Card-Payments'   : ('Assets:ZSA-Matched:Credit-Card-Payments'  ,  6),
     'Assets:Zero-Sum-Accounts:Temporary'              : ('Assets:ZSA-Matched:Temporary'             , 90),
      }
     }"

As the example shows, the argument is a dictionary where the keys are the set
of accounts on which the plugin should operate. The values are
(target_account, date_range), where the target_account is the account to which
the plugin should move matched postings, and the date_range is the range over
which to check for matches for that account.

TODO:
- allow config using account metadata
- take plugin params from metadata (including date_range)
- optionally create a linking metadata (or a beancount-link) between matches

"""

import time
import collections
from ast import literal_eval
import datetime
from collections import defaultdict
import cProfile, pstats

from beancount.core import data
from beancount.core import flags
from beancount.core import getters

DEBUG = 0

__plugins__ = ('zerosum', 'flag_unmatched',)

# replace the account on a given posting with a new account
def account_replace(txn, posting, new_account):
    # create a new posting with the new account, then remove old and add new
    # from parent transaction
    new_posting = posting._replace(account=new_account)
    txn.postings.remove(posting)
    txn.postings.append(new_posting)

def zerosum(entries, options_map, config):
    """Insert entries for unmatched transactions in zero-sum accounts.

    Args:
      entries: a list of entry instances

      options_map: a dict of options parsed from the file (not used)

      config: Python dict with two entries:

      - 'zerosum_accounts': maps zerosum_account_name -> (matched_zerosum_account_name,
        date_range). matched_zerosum_account_name is optional, and can be left blank. If
        left blank, the name of the matched account is derived from the
        zerosum_account_name, by performing the string replacement specified by
        'account_name_replace' (see below)

      - 'account_name_replace': tuple of two entries. See above

      - 'flag_unmatched': bool to control whether to flag unmatched
        transactions as warnings (default off)

      See example for more info.

    Returns:
      A tuple of entries and errors.

    """

    def find_match():
        '''Look forward to find a match, until date range is exceeded'''
        max_date = txn.date + datetime.timedelta(days=date_range)

        for j in range(i, len(zerosum_txns)):
            t = zerosum_txns[j]
            if t.date > max_date:
                return None
            for p in t.postings:
                if (abs(p.units.number + posting.units.number) < EPSILON_DELTA
                    and p.account == zs_account):
                    return (p, t)
        return None

    if DEBUG:
        # pr = cProfile.Profile()
        # pr.enable()
        start_time = time.time()

    config_obj = literal_eval(config) #TODO: error check
    zs_accounts_list = config_obj.pop('zerosum_accounts', {})
    (account_name_from, account_name_to) = config_obj.pop('account_name_replace', ('', ''))

    new_accounts = set()
    zerosum_postings_count = 0
    match_count = 0
    EPSILON_DELTA = 0.0099

    # Build zerosum_txns_all for all zs_accounts, so we iterate through entries only once (for performance)
    zerosum_txns_all = defaultdict(list)
    for entry in entries:
        if isinstance(entry, data.Transaction):
            for zs_account, _ in zs_accounts_list.items():
                if any(posting.account == zs_account for posting in entry.postings):
                    zerosum_txns_all[zs_account].append(entry)
                    zerosum_postings_count += 1
                    # count doesn't account for multiple matching postings, but is close enough

    for zs_account, (target_account, date_range) in zs_accounts_list.items():
        if not target_account:
            target_account = zs_account.replace(account_name_from, account_name_to)
        zerosum_txns = zerosum_txns_all[zs_account]

        # for each posting in each transaction, attempt to find a match. Replace account names in each each
        # matched posting pair
        for i in range(len(zerosum_txns)):
            txn = zerosum_txns[i]
            reprocess = True
            while reprocess: # necessary since this entry's postings changes under us when we find a match
                for posting in txn.postings:
                    reprocess = False
                    if posting.account == zs_account:
                        match = find_match()
                        if match:
                            # print('Match:', txn.date, match[1].date, match[1].date - txn.date,
                            #         posting.units, posting.meta['lineno'], match[0].meta['lineno'])
                            match_count += 1
                            account_replace(txn,      posting,  target_account)
                            account_replace(match[1], match[0], target_account)
                            new_accounts.add(target_account)
                            reprocess = True
                            break

    new_open_entries = create_open_directives(new_accounts, entries)

    if DEBUG:
        elapsed_time = time.time() - start_time
        print("Zerosum [{:.1f}s]: {}/{} postings matched from {} transactions. {} new accounts added.".format(
            elapsed_time, match_count*2, zerosum_postings_count, len(entries), len(new_open_entries)))
        # pr.disable()
        # pr.dump_stats('out.profile')

    return entries + new_open_entries, []


def flag_unmatched(entries, unused_options_map, config):
    '''Iterate again, to flag unmatched entries'''

    config_obj = literal_eval(config)
    if not config_obj.get('flag_unmatched'):
        return (entries, [])

    new_entries = []
    zs_accounts = config_obj['zerosum_accounts'].keys()
    for entry in entries:
        if isinstance(entry, data.Transaction):
            for posting in entry.postings:
                if posting.account in zs_accounts:
                    entry = entry._replace(flag=flags.FLAG_WARNING)
                    break
        new_entries.append(entry)
    return new_entries, []


def create_open_directives(new_accounts, entries):
    meta = data.new_metadata('<zerosum>', 0)
    # Ensure that the accounts we're going to use to book the postings exist, by
    # creating open entries for those that we generated that weren't already
    # existing accounts.

    # TODO: should ideally track account specific earliest date. Using this as a proxy
    earliest_date = entries[0].date
    open_entries = getters.get_account_open_close(entries)
    new_open_entries = []
    for account_ in sorted(new_accounts):
        if account_ not in open_entries:
            meta = data.new_metadata(meta['filename'], 0)
            open_entry = data.Open(meta, earliest_date, account_, None, None)
            new_open_entries.append(open_entry)
    return(new_open_entries)

