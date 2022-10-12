# Assignment 3 

## 1 - Compare the module/bundle concepts of maven and OSGi, what are the similarities and differences. Give examples of why/how the extra expressivity of (the meta-data of) OSGi bundles are useful.

In maven a module's requirements and other information about the module are declared in a POM.xml (Project Object Model) file, in the root of the project folder. Also in the POM file, are all of the project's dependencies to other maven modules with a specific version number. On the other hand, in OSGi a bundle consists of a JAR file and a MANIFEST.MF file. The MANIFEST.MF file includes which other OSGi bundles this bundle needs to import and what the bundle exports, as well as a unique symbolic name as to not be confused with other bundles. 

A benefit of OSGi's extra expressivity is that it eliminates the risk for dependencies declared in multiple modules, with different versions, to interact with each other. Which could lead to problems in the code. In Maven if a dependancy is declared multiple places, the highest version is chosen, which can lead to unforeseen situations.

## 2 - In the dict example project @ https://gitlab.stud.idi.ntnu.no/TDT4250/examples/-/tree/master/dict-ws, a dictionary service is made modular and extensible. Discuss the three variants in terms of the Modularity Maturity Model linked to by https://www.infoq.com/news/2011/09/mmm-osgi/

The first variant is level 1 (Ad Hoc) in the Modularity Maturity Model, as it only includes one bundle and it is monolothic. The second variant has split the original tdt4250.dict1.servlet bundle into two independant bundles. This makes it a bit more modular, but it is inflexible. With this, I would put the second variant into the level 2 category (Modules). Last but not least, the third variant. The third variant consists of multiple different bundles, that have minimal dependencies. This variant also uses injections. I would therefore put the third variant into Level 4 (Loose coupling).

## 3 - Group project
In the group project we used Xtend and Xtext to create a DSL, that created .jsx React components from our specified language. We found the setup process a bit hard, but once we started actually implementing the DSL it was very fun and educational. From this project I have learned a lot about how easily I can setup and create my own language to solve specific tasks in a more effective way, also I have seen how model-driven code generation can aid in developing a large project as it generates a lot of boilerplate code for you.