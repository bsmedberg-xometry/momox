# momox - The Mongo Model Layer for Xometry

A mongo model layer for python that is fast, reliable, and safe.

## Design goals

* Be fast
  * Don't load data you don't have to! Make it easy and normal to fetch only the data you need from mongo.
  * Don't validate data you don't have to.
  * Don't dereference by default. Any dereference of a collection should be explicitly visible in client code.
* Reliable
  * Throw good errors.
  * Accessing a field that doesn't exist should be easy.
  * Referencing a field you didn't fetch should throw, not apply meaningless defaults.
* Safe
  * Make it normal to hand out read-only model data so that clients can't make accidental changes.
  * Make data changes deliberately visible.
  * Don't support dynamic polymorphism. Static inheritance is ok though!

Much of this project is inspired by and some was copied from [pymodm](https://github.com/mongodb/pymodm).
