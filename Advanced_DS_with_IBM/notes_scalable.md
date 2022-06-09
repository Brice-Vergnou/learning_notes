## Week 1 :

Just setting up an IBM cloud account to be able to use an Spark server later on

## Week 2 :

**Types of data storage :**

|   | SQL | NoSQL      | ObjectStorage |
| :-----------: | :-----------: | :-----------: | :-----------: |
! low | very low 
| Scalability   | low        | high | very high
| Query speed      | high       | low | very low
| Flexibility   | low        | high  | very high

**SQL :**
* Pros :
  * Well known, well establish
  * High integrity and data normalization
  * Fast indexed access
  * Open standard
* Cons : 
  * Change of schema needs DDL ( [data definition language](https://www.techopedia.com/definition/1175/data-definition-language-ddl) )
  * Hard to scale
  * High storage cost

**NoSQL :** 
* Pros:
  * Dynamic schema
  * Low storage cost
  * Linearly scalable
* Cons :
  * No data normalization or integrity
  * Less established
  * Slower access ( JSON-formatted )
  
**ObjectStorage :**
* Pros :
  * Very low storage cost 
  * Linearly scalable
  * Seamless schema migration, schema-less
  * Open standard storage
  
* ApacheSpark -> Java virtual machine written in Scala
* One JVM per CPU core
* Data is either in the same cluster (Network attached storage), or attached to each computer (JBOD) and shared in fractions  thanks to HDFS ( Hadoop Distributed file system ) 

![image](https://user-images.githubusercontent.com/86613710/170888929-3b4a2813-dd1c-4457-9d61-7e548bd152c0.png)

* ApacheSpark uses RDD ( Resilien Distributed Data )
* in-memory but spillable to disk + lazy evaluation ( functions are executed if their computations is necessary )
* **ApacheSpark is implicitly parallel**
* 
