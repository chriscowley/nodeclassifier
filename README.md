# Node Classifier

[![Build Status](https://travis-ci.org/chriscowley/nodeclassifier.svg?branch=develop)](https://travis-ci.org/chriscowley/nodeclassifier)

App and REST API for classification of Nodes for use in Puppet. Enables the
assignment of Roles and Profiles to nodes based on attributes other than
hostname.

The basic idea is that the node sends a bunch if identifying data: serial #,
model #, brand, motherboard type, etc. Based on this info the node classifier
will return a hash including a _role_:

```
{
  'role': 'something',
}
```

This can then be collected with a custom fact and used to assign modules to
a node.

This is inspired by work done by [Rob Nelson](http://rnelson0.com/2014/07/14/intro-to-roles-and-profiles-with-puppet-and-hiera/) and [Jordan Sissel](https://github.com/jordansissel/puppet-examples/tree/master/nodeless-puppet)

## Install

No idea yet, TBC

## Contact Me

Email me at [chriscowleysound@gmail.com](mailto:chriscowleysound@gmail.com)

# Changelog

## Version 0.1.0

* Initial version
