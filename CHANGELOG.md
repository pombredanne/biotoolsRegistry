# Changelog
All notable changes to *bio.tools* will be documented here.

Credits to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]
### Added
### Changed
### Removed
### Fixed
### Deprecated
### Security


## Apr 10th 2019
### Added
- [(142)](https://github.com/bio-tools/biotoolsRegistry/issues/142) **Added bio.tools homepage**: including general information, key facts in boxes, EDAM-based navigation on highly used operations and topics, National & institutional credits, new footer

- [(418)](https://github.com/bio-tools/biotoolsRegistry/issues/418) **Improved and extended "About" page**

- [(416)](https://github.com/bio-tools/biotoolsRegistry/issues/416) **Addition of high-quality annotations for proteomics**: annotations including operations, and input/output data types and formats, in support of https://doi.org/10.1093/bioinformatics/bty646

- [(406)](https://github.com/bio-tools/biotoolsRegistry/issues/406) **Labelling of official ELIXIR service assignations**: labelling in Tool Cards of official ELXIIR [Core data resource](https://www.elixir-europe.org/platforms/data/core-data-resources), [ELIXIR Deposition Database](https://www.elixir-europe.org/platforms/data/elixir-deposition-databases) and [Recommended Interoperability Resource](https://www.elixir-europe.org/platforms/interoperability/rirs)

- [(405)](https://github.com/bio-tools/biotoolsRegistry/issues/405) **Inclusion of ELIXIR Node & Platform annotations**: annotation as credits of [ELIXIR Node](https://www.elixir-europe.org/about-us/who-we-are/nodes) and [Platforms](https://www.elixir-europe.org/platforms) for tools and databases in the [ELIXIR Nodes Service Delivery Plans](https://www.elixir-europe.org/services).

- [(207)](https://github.com/bio-tools/biotoolsRegistry/issues/207) **Labelling Tool Cards based on broken homepage URL**: using a reasonably sophisticated handling of error codes and other HTTP messsages, a Tool Card may be labelled as down (or this label removed if it becomes available again).  Tools may be labelled (manually) as permanently down where we know (*i.e.* have been told) the tool is now officially obsolete. (partial implementation)

- [(139)](https://github.com/bio-tools/biotoolsSchema/issues/139), [(141)](https://github.com/bio-tools/biotoolsRegistry/issues/141) **Extended valid download types**: Add "Dowwnloads page" and "Other" as valid downloads type

- [(132)](https://github.com/bio-tools/biotoolsSchema/issues/132), [(112)](https://github.com/bio-tools/biotoolsschema/issues/112) **Extended valid documentation types**: Add "FAQ" and "Release notes" as valid documentation type

- [(129)](https://github.com/bio-tools/biotoolsschema/issues/129), [(138)](https://github.com/bio-tools/biotoolsschema/issues/138), [(128)](https://github.com/bio-tools/biotoolsSchema/issues/128) **Extended valid link types**: Add "Galaxy service", "Discussion forum" and "Other" as valid link types

- [(422)](https://github.com/bio-tools/biotoolsRegistry/issues/422) **Added tool type to entries lacking this annotation**

- [(420)](https://github.com/bio-tools/biotoolsRegistry/issues/420) **Added topic to entries lacking this annotation**


### Changed
- [(357)](https://github.com/bio-tools/biotoolsRegistry/issues/357) **Manually verify tool IDs (added since latest verification)**: ensuring tool IDs (based on tool name) are sensible, and consolidating / resolving duplicates and redundancies arising from this.

- [(282)](https://github.com/bio-tools/biotoolsRegistry/issues/282) **Refactoring of names & IDs of tools imported automatically via Galaxy**: using Galaxy Pasteur instance as a trial, refactoring of names & IDs and de-duplications were necessary, to ensure "canonical" tool descriptions.

- [(419)](https://github.com/bio-tools/biotoolsRegistry/issues/419) **Improved curation of high usage tools**

- [(417)](https://github.com/bio-tools/biotoolsRegistry/issues/417) **Clean-up of high-level annotations** *e.g.* Software engineering, Data management, Bioinformatics, Database management, Data integration and warehousing, Data architecture, analysis and design, Omics, Informatics, Algorithms (quite a lot of these were assigned erroneously)

- [(407)](https://github.com/bio-tools/biotoolsRegistry/issues/407) **Credits tab is now Credits & Support**

### Removed

### Fixed

- [(299)](https://github.com/bio-tools/biotoolsRegistry/issues/299) **Systematic check & fix of broken (numeric-appended) IDs**

- [(411)](https://github.com/bio-tools/biotoolsRegistry/issues/411) **Tool IDs no longer contain "beta" or "alpha"**: 20+ of these (names may (temporarily) include "beta", "alpha" etc. but not the IDs).

- [(413)](https://github.com/bio-tools/biotoolsRegistry/issues/413) **Count of search results now cleared correctly**

### Deprecated

### Security


## Dec 14th 2018
### Added
- [(126)](https://github.com/bio-tools/biotoolsRegistry/issues/126) **Upgraded data model**: support for [biotoolsSchema 3.0.0](https://github.com/bio-tools/biotoolsSchema/tree/master/versions/biotools-3.0.0) which is simpler and more expressive than the previous version.  It is fully supported (all schema fields) in *bio.tools* (content, UI and API were refactored).
- [(327)](https://github.com/bio-tools/biotoolsRegistry/issues/327), [(120)](https://github.com/bio-tools/biotoolsRegistry/issues/120), [(63)](https://github.com/bio-tools/biotoolsRegistry/issues/63) **Interactive annnotations**: clicking on a label for EDAM annotations (topic, operation, data or format) and biotoolsSchema elements (currently just ``collectionID``) now perform a search within *bio.tools*.
- [(317)](https://github.com/bio-tools/biotoolsRegistry/issues/317), [(117)](https://github.com/bio-tools/biotoolsRegistry/issues/117), [(70)](https://github.com/bio-tools/biotoolsRegistry/issues/70), [(395)](https://github.com/bio-tools/biotoolsRegistry/issues/395) **Tool tips** on tool descriptor tags (maturity, cost *etc.*) now explain in plain english what these mean, and provide links to schema docs where necessary.
- [(390)](https://github.com/bio-tools/biotoolsRegistry/issues/390) Much cleaner presentation of **publication information** in Tool Cards, including rendering of Altmetric & Dimensions badges for all publications.
- [(392)](https://github.com/bio-tools/biotoolsRegistry/issues/392) [Dimensions badge](https://badge.dimensions.ai/) added to Tool Cards to render **citation information** and link out to **research insights**.
- [(80)](https://github.com/bio-tools/biotoolsRegistry/issues/80) Links to **TeSS training** events and materials (from [TeSS](https://tess.elixir-uk.org)) added (partial implementation).
- **Help for curators**:  added links to *bio.tools* [Curators Guide](https://biotools.readthedocs.io/en/latest/curators_guide.html) from registration interface.
- [(374)](https://github.com/bio-tools/biotoolsRegistry/issues/374) Added **tool operations** to compact / mini-card view
- [(391)](https://github.com/bio-tools/biotoolsRegistry/issues/391) New ELIXIR-branded  **bio.tools** logo replacing vanilla ELIXIR logo.
- [(8)](https://github.com/bio-tools/biotoolsRegistry/issues/8) Data entry fields in registration interface now include **example values**.
- [(128)](https://github.com/bio-tools/biotoolsRegistry/issues/128) **Comments on credits** now rendered.
- [(58)](https://github.com/bio-tools/biotoolsRegistry/issues/58) **Output format type** can now be specified as flag on URL (for data download from API)
- [(308)](https://github.com/bio-tools/biotoolsRegistry/issues/308) Added button to confim **subdomain deletion**.


### Changed
- greatly enriched API parameters allow **precise queries** over tool function and other metadata.  See [API reference](https://biotools.readthedocs.io/en/latest/api_reference_dev.html) and [API Usage Guide](https://biotools.readthedocs.io/en/latest/api_usage_guide_dev.html).
- [(385)](https://github.com/bio-tools/biotoolsRegistry/issues/385) **Enhanced faceting** in the search box allowing specific search with autocompletion for operation, tool type, language, accessibility, cost and license.
- [(302)](https://github.com/bio-tools/biotoolsRegistry/issues/302) **Lower barrier to registration** mandating only tool name, short desription and homepage (as per [biotoolsSchema 3.0.0](https://github.com/bio-tools/biotoolsSchema/tree/master/versions/biotools-3.0.0)), removing the need to handle suggestions for tool additions
- [(383)](https://github.com/bio-tools/biotoolsRegistry/issues/383) Tool tips on **function diagram** explain to users the meaning of the annotations and behaviour when clicked.
- [(60)](https://github.com/bio-tools/biotoolsRegistry/issues/60) Much cleaner rendering and use of **publication information**.
- [(312)](https://github.com/bio-tools/biotoolsRegistry/issues/312) **Subdomain names** now support '-' character allowing *e.g.* for names that reflect hiearchical structure, or just cleaner looking subdomains *e.g.* https://rare-diseases.bio.tools/.
- [(303)](https://github.com/bio-tools/biotoolsRegistry/issues/303) Sorting of data formats for more **convenient term picking** during registration.
- [(374)](https://github.com/bio-tools/biotoolsRegistry/issues/374) Changed **colour of UI elements** to match the [EDAM colour scheme](https://github.com/edamontology/edamontology/issues/340)
- [(277)](https://github.com/bio-tools/biotoolsRegistry/issues/277) Validation / save state now made clear via button colouring and ticks in UI.
- [(389)](https://github.com/bio-tools/biotoolsRegistry/issues/389) **Homepage URL** more prominent in Tool Card
	
### Removed
- [(379)](https://github.com/bio-tools/biotoolsRegistry/issues/379) Removed (now uneccessary) rendering of "None" for version information.
- [(375)](https://github.com/bio-tools/biotoolsRegistry/issues/375) Replaced webpage at https://bio.tools/schema with redirect to [biotoolsSchema repo](http://github.com/bio-tools/biotoolsschema)

### Fixed
- [(300)](https://github.com/bio-tools/biotoolsRegistry/issues/300), [(275)](https://github.com/bio-tools/biotoolsRegistry/issues/275) Prevented accidental creation of **duplicate entries**, with clean assignment of **biotools toolIDs**.
- [(386)](https://github.com/bio-tools/biotoolsRegistry/issues/386) Fixed 160 **tool descriptions** that were invalid according to [biotoolsSchema 3.0.0](https://github.com/bio-tools/biotoolsSchema/tree/master/versions/biotools-3.0.0).
- [(234)](https://github.com/bio-tools/biotoolsRegistry/issues/234) Fixed 173 **EDAM annotations** where a term was given with no corresponding URI.
- [(384)](https://github.com/bio-tools/biotoolsRegistry/issues/384) Fixed overly long **collection IDs** that were invalid according to [biotoolsSchema 3.0.0](https://github.com/bio-tools/biotoolsSchema/tree/master/versions/biotools-3.0.0).
- [(230)](https://github.com/bio-tools/biotoolsRegistry/issues/230) Fixed bugs in handling searches using terms containing **diacritics**.
- [(371)](https://github.com/bio-tools/biotoolsRegistry/issues/371), [(367)](https://github.com/bio-tools/biotoolsRegistry/issues/367), [(295)](https://github.com/bio-tools/biotoolsRegistry/issues/295) Misc. **content clean-ups**.
- [(343)](https://github.com/bio-tools/biotoolsRegistry/issues/343) Fixed bug in search for formats.
- [(337)](https://github.com/bio-tools/biotoolsRegistry/issues/337), [(229)](https://github.com/bio-tools/biotoolsRegistry/issues/229), [(281)](https://github.com/bio-tools/biotoolsRegistry/issues/281) Fixed invalid or inconsistent DOIs and DOI validation.
- [(322)](https://github.com/bio-tools/biotoolsRegistry/issues/322), [(274)](https://github.com/bio-tools/biotoolsRegistry/issues/274), [(14)](https://github.com/bio-tools/biotoolsRegistry/issues/14) Fixed bug / inconsistencies in registration of publication information, with improved error reporting.
- [(321)](https://github.com/bio-tools/biotoolsRegistry/issues/321) Fixed bug in controlled vocabularies.
- [(310)](https://github.com/bio-tools/biotoolsRegistry/issues/310) Fixed restriction on data retrieval via API (10,000 result limit no longer applies)
- [(298)](https://github.com/bio-tools/biotoolsRegistry/issues/298) Fixed mix-up of "function" and "operation" in registration interface.

### Deprecated

### Security
