Rename accounts plugin for Beancount
------------------------------------

Plugin to rename accounts. Takes a list of account pairs to rename. Here are some
examples where this can be useful.

This is useful when one wants two different views (reports) into the same set of
transactions. Renames in this plugin can be easily turned on or off (by manually
commenting them out in your beancount plugin directive) depending on the type of
reporting desired. Here is an example where this is useful:

`Expenses:Taxes -> Income:Taxes`

This rename allows taxes to avoid cluttering and dominating the Expense reports (and
thus rendering them less useful), and simultaneously reports net (after-tax) income.
Without the rename, of course, the view of gross income and expenses including taxes
becomes available.

Of course, the right set of queries can also give you these reports renaming. However,
renaming allows you to take advantage of standard, built-in reporting tools. For
example, fava's treemap/sunburst expense plots would not work out of the box on a
custom query. Renaming solves this problem.


Configuring
-----------

Example to include in your beancount file:

```python
plugin "beancount_reds_plugins.rename_accounts.rename_accounts" "{
 'Expenses:Taxes' : 'Income:Taxes',
 'Expenses:Employer-Paid-Benefits' : 'Income:Employer-Paid-Benefits',
 }"
```

This assumes you've checked out the repo to: `plugins/beancount_plugins_redstreet`

The strings on the left are string-matched against accounts. `Expenses:Taxes:Federal`
will be renamed to `Income:Taxes:Federal` in the example above.

Account opening entries will be added to beancount automatically if needed. Continuing
the example above, an open directive will automatically be inserted for
`Income:Taxes:Federal` if needed.
