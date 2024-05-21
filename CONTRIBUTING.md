# Contributing to preoccupied.koji-typing

Your contributions will be licensed under the GPL v3.

Create an issue against the Github project indicating what you want to
work on, and whether it is a bug fix or an enhancement.

Fork the project and commit your changes there. Then submit a pull
request when you're ready. You're also welcome to create your PR as a
draft if you simply want to make it clear that the issue you've filed
is actively being worked on, but if your work isn't yet ready to be
merged.


## make yourself known

Your PR should add yourself to the bottom of the AUTHORS.md file if
you are not already present in it. Please try to use the same email
address that you've configured your git commits with.


## no new types in stubs

Do not introduce signatures into typing stubs which are not in the
runtime packages. This is especially relevant around type definitions
for Callable and TypedDict. Any new type definitions must be made in
the koji_types pacakge or sub-module.


## allowlist and futurelist

For signatures which are particularly difficult for stubtest to
validate (such as those with a default value that differs from machine
to machine) add them to allowlist.

For signatures which are different between the most recent GA of koji
vs. the upstream git master branch, add them to the futurelist. This
means new functions, removed functions, or changed signatures


## comment incompatibilities

When koji makes an API change add the new form with a comment which
clearly states the version that introduced the change. For removals,
comment out the original definition rather than deleting it outright.

in addition, if it's possible to express the API change using an
overload such that both the original and new signatures are present,
then do so. Again, use a comment on the new signature to indicate the
version it was introduced in.
