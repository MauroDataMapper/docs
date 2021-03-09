The team at Oxford have been engaged in research and development of Metadata Registries for more than a decade; the Mauro Data Mapper is the
represents the third generation of this technology. In the first generation, we used the eXist database as a simple store of XML representations of
metadata items as individual attributes with aribtrary XML document types. This version of the catalogue did not make use of or enforce the
constraints of a data modelling language, and the approach to semantic linkage was through classification, rather than individual assertions of
refinement. It was applied successfully in two large projects, but proved difficult to maintain.

The second generation of the technology was developed for the National Institute for Health Research (NIHR) Health Informatics Collaborative: a
national programme aimed at facilitating the re-use of routinely-collected hospital data for medical research. This version of the catalogue allowed
arbitrary links, and included some of the features of the data modelling language presented here, but without a consistent, formal interpretation.

The design included our principle that models should be the units of context and versioning. However, links were not contained within attributes,
classes, or even models, and hence not subject to model finalisation, making it impossible to ensure consistency. Furthermore, it was possible to
‘import’ arbitrary items across models, without any guarantee that the definition of these items was independent of context.

This third generation of the technology was developed from scratch, based on the experience of the previous implementations, and—crucially—developed
in parallel with the formal semantics presented above. The result was a catalogue in which it was possible to guarantee consistency of definitions,
and to achieve a greater degree of scalability through automation and federation.

The team have been engaged with the standards community - in particular the development of
the [ISO/IEC 11179/3 standard for metadata registration](http://metadata-standards.org/11179/), and related specifications.  While the model 
defined in this standard is more closely aligned with the original generation of the tool, all subsequent implementations of Mauro maintain 
compliance with this standard for interoperability.    
