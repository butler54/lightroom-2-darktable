# lightroom-2-darktable

A personal project to help transition from Adobe Lightroom to darktable. Build for the particular issues I have in mind.

**THIS IS CURRENTLY A WORK IN PROGRESS**

## Why?

I've used lightroom for many years. It's a great tool. However, I'm not getting as much value as I like from it for a number of reasons:

1. Lightroom classic can't sync to my iPad anymore
1. I'm using it sporadically
1. I barely use photoshop.

99% of my edits are in lightroom or in external effects (DXO labs film effects). I don't get value from photoshop today.

This has led to a desire to migrate to [darktable](https://www.darktable.org/) which is FOSS. However, I need to deal with the legacy of multiple lightroom catalogs and a bit of a mess.

## Questions that need to be answered:

### Single catalog questions

1. Has lightroom generated xmp sidecars for all the images xmp sidecars exist for? and list the ones it has not done so?
1. Which images are in lightroom but not in a collection?
1. Which images are in mulitiple collections?
1. Which images are missing?
1. Which images are in lightroom's directory tree but NOT in the lightroom database?
1. Have duplicate images being imported duplicate as measured by image hash.

### Multiple catalog questions

1. Are any collection names, excluding a reference list, duplicated
1. Are any images duplicated across catalogs?
1. Across multiple catalogs are images duplicated?
### Import actions:

1. For a lightroom collection create a folder tree, including `xmp` sidecars for that collection using copy.
1. For a set of lightroom collections create a folder tree for each as above.
1. For a set of lightroom collections do the same, however, moving files opportunistically and therefore guaranteeing no duplicates and skipping over files
1. For any of the above, do so, however, exclude images that have been flagged negatively

## Assumptions

### Design assumptions based on my environment

1. Multiple lightroom catalogs
1. File trees have been moved; potentially multiple times.
1. No Windows considered. Assume that this is been run on a mac or linux.
1. Don't rely on file system dates.

### Version assumptions

1. Lightroom classic only. Tested against catalog v 13 versions.

## Design choices:

1. Python: Why? I'm most comfortable with it.
1. Make the collections ready for Darktable but import into darktable using darktable native interfaces: Keep the moving parts down

## License

`lightroom-2-darktable` is distributed under the terms of the [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html) license.
