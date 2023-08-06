> *buzzword* is a web app for corpus linguistics, built with [buzz](https://github.com/interrogator/buzz) as a backend. *buzzword* allows you to parse, search and visualise language datasets in your browser. The tool is soon to be hosted by UZH, but can also be run locally (see [here](run.md) for instructions).

*buzzword* consists of two main pages: a *Start* page, where you select or upload a corpus, or get help; and an *Explore* page, which provides an interface for working with a parsed/annotated corpus. The *Explore* page is divided into tabs for different tasks, such as searching, building frequency tables, visualising and concordancing. Below are instructions for each page and tab.

# Start page

The main page of the tool allows you to select a pre-loaded corpus, or upload your own. If you want to browse a pre-loaded corpus, simply click its name in the table.

If you want to upload your own data, you can upload plain text files (which will be parsed), plain text with metadata (which will also be parsed), or CONLL-U formatted files, which will be loaded directly into the tool without any processing.

For information about how to create metadata-rich corpora, see [here](building.md). Once you've done that, you can simply upload one or more created files via the drag-and-drop interface. Then, simply give the corpus a name, select the language, and hit *Upload and parse*. Parsing shouldn't take long, even for large and metadata-rich corpora. After parsing, a link to the corpus will become available in the table.

# Explore page

Once you have either uploaded or selected a pre-loaded corpus, you will be taken to the *Explore* page. This page provides an interface for searching and visualising a dataset.

## Dataset view

In this view, you can see the loaded corpus, row by row, with its token and metadata features. Like the other tables in *buzzword*, this one is interactive: you can filter, sort and remove rows and columns as you wish. To filter, just enter some text into one of the blank cells above the first table row. More advanced kinds of filtering strings are described [here](https://dash.plot.ly/datatable/filtering). Note that filters are just temporary views of the corpus, and are not applied permanently to your data; use the *Search* functionality to create subsets of data that can be searched further, concordanced or plotted.

### Searching

The *Dataset tab* is the place where you search your dataset. In *buzzword*, because you can search within search results, the best way to find what you're looking for is usually to "drill-down" into the data by searching multiple times, rather than writing one big, complicated query.

**Feature to search**: in the leftmost dropdown field, you select the feature you want to search (word form, lemma form, POS, etc). Each of these options targets a token or metadata feature, except *Dependencies*, which is used to search the dependency grammar with which a corpus has been parsed. To start out, select something simple, like *Word*, so that your search string will be compared to the word as it was written in the original, unparsed text.

**Query entry**: in the text entry field, you provide a case-sensitive regular expression that you want to match. The only exception to this is if you are searching *Dependencies*, in which case you will need to use [the depgrep query language](depgrep.md). If you're new to regular expressions, and just want to find words that exactly match a string, enter `^word$`. The caret (`^`) denotes 'start of string', and the dollar sign (`$`) denotes the end of string. Without the dollar sign, the query would match not only *word*, but *wordy*, *wording*, *word-salad*, and so on. Once you get used to using regular expressions, you'll find them very powerful, so learning to write them is a valuable skill! If you want your search to be case-insensitive, the best way to do this is to begin your query with `(?i)`, which denotes case insensitivity in the language of regular expressions.

**Inverting searches**: finally, you can toggle result inversion using the toggle switch (i.e. return rows *not matching* the search criteria). This is especially useful if you want to remove particular unwanted results. For example, if you want to match any pronoun but *me*, rather than writing a regular expression to match every other pronoun (*I*, *you*, *he*, etc.), simple search for any token whose part of speech is *PRP*, and then run another search for any word matching *me*, inverting the result.

Once your query is formulated, hit *Search*. Search time depends mostly on how many items are returned, though very complex *depgrep* queries can also take a few seconds.

### Working with search results

When the search has completed, the table in the *Dataset* tab will be reduced to just those rows that match your query. At the top of the tool, you'll see that your search has entered into the *Search from* space, translated into something resembling natural English. Beside the search is a bracketed expression telling you how many results you have. This component has the format:

`(absolute-frequency/percentage-of-parent-search/percentage-of-corpus)`

Whatever is selected in the *Search from* dropdown is now the dataset to be searched. Therefore, if you search again with the current search selected, you will "drill down", removing more rows as you go. So, if you are interested in nouns ending in *ing* that do not fill the role of *nsubj*, you can search three times:

1. Wordclass matching `NOUN`
2. Word matching `ing$`
3. Function mtching `nsubj`, inverted

Alternatively, you could write one *depgrep* query:

```
X"NOUN" = w/ing$/ != F"nsubj"
```

If you want to learn to use the *depgrep* language, you can view the [*depgrep* page](depgrep.md) for a guide to query construction.

At any time, if you want to delete your search history, you can use the 'Clear history' button to forget all previous searches, returing the tool to its original state.

## Frequencies view

In contrast to other tools, *buzzword* separates the processes of searching datasets and displaying their results. This gives you the flexibility to display the same search result in different ways, without the need for performing duplicated searches. So, once you are happy with a search result generated in the *Dataset* tab, you can move to the *Frequencies* tab to transform your results into a frequency table.

### Tabling options

To generate a frequency table, start by selecting the correct dataset from the *Search from* dropdown menu at the top of the tool. These are the results you will be calculating from. You can select either the entire corpus, or a search result generated in the *Dataset* tab.

Next, you need to choose which feature or features you want to use as the column(s) of the table. Multiple selections are possible; for example, you can select `Word` and then `Wordclass` to get results in the form: `happy/adj`.

After selecting columns, select which feature should serve as the index of the table. You don't have to use `Filename` here: you can model things like *lemma by speaker* or *Function by POS*. Multiple selections are not possible here (though they are in the *buzz* backend, if you would prefer to use that).

Next, choose how you would like to sort your data. By default, the most frequent items appear first. But, you can sort by infrequent (i.e. reverse total), alphabetically, and so on. Particularly special here are *increase* and *decrease*. These options use linear regression to figure out which items become comparatively more common from the first to last items on the x-axis. They are particularly useful when your choice for table index is sequential, such as chapters of a book, scenes in a film, or dates.

Finally, choose what kind of calculation you would like. The default, *Absolute frequency*, simply counts occurrences. You can also choose to model relative frequencies, using either this search or the entire corpus as the denominator. What this means is that if you have searched for all nouns, you can calculate the relative frequency of each noun relative to all nouns (*Relative of result*), or each noun relative to all tokens in the corpus (*Relative of corpus*).

Alternatively, you can also choose to calculate keyness, rather than absolute/relative frequency. Both [log-likelihood](http://ucrel.lancs.ac.uk/llwizard.html) and percentage-difference measures are supported. These measures are particularly useful as means to find out which tokens are unexpectedly frequent or infrequent in the corpus.

### Generating tables: a note on performance

Once you've chosen your parameters, hit *Generate table* to start the tabling process. Like searching, the calculations themselves are fairly fast. What might take some time, however, is displaying a result with many rows/columns. So, it is important to bear in mind when tabling that some choices can lead to unmanageably large results, which could potentially cause memory-related errors: if you choose to display *Word*, *Filename*, *Sent #* and *Token #* as columns, for example, you will be generatng a column for every single token in the corpus. Before generating a table, it's therefore wise to quickly consider the expected size of the output.

### Editing the *Frequencies* table

Whenever you edit the frequencies table (i.e. deleting rows or columns), the changes will be reflected in the underlying data. So, charts generated from this table will not contain the deleted rows and columns. Note, however, that deleting rows and columns will not lead to recalculation of relative frequencies. If you want to recalculate relative frequencies, you should instead run a new sub-search from the *Dataset* view, skipping the rows and/or columns you don't want.

### Downloading the table

You can click the *Download* link near the bottom of the page to download the entire frequency table in CSV format. You can then load this file into software like Excel in order to explore it further.

### Chart view

Once you have a table representing the results you're interested in, you can go to the Chart tab to visualise the result. Visualisation is easy: just select the plot type, the number of items to display, and whether or not you want to transpose (i.e. invert) the rows and columns.

All figures are interactive, so go ahead and play with the various tools that appear above the charts. Using these tools, you can also choose to save the figure to your hard drive for access outside of *buzzword*,

Note that there are multiple chart spaces. Just click '*Chart #1*' to fold this space in and out of view. Each space is completely independent from the others. You can therefore visualise completely different things in each.

### Concordance view

Concordances, or *Keywords-in-context* (KWIC), involve aligning each search result in a column, displaying their co-text on either side. In *buzzword*, concordances are another way of viewing a search result. Therefore, rather than directly running a concordance query like you do in most other tools, you first run a search in the *Dataset* view, and then use the *Concordance* tab to display this result as a concordance.

To display a concordance, first, select the search result you want to visualise from the *Search from* dropdown menu at the top of the page. Then, select how you would like to format your matches. Like when making frequency tables, you can format matches using multiple token features. One popular combination is *word/POS*, but there are plenty more combinations that might be useful, too!

## Bugs, features and notes

*buzzword* is a new tool, and still a work in progress. If you find a bug, or need a feature in order to use the tool more effectively, please create an *Issue* at [the project's repository](https://github.com/interrogator/buzz).

In terms of future development, the first priority is on making the tool stable and useful for researchers. After this, there are new planned features, such as language modelling and word embeddings, where you can enter text and check its similarity to texts inside the corpus. Also planned is the ability to create permalinks, so that you can quickly share results and charts with others.
