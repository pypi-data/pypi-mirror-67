# FastCDC

[![Version](https://img.shields.io/pypi/v/fastcdc.svg)](https://pypi.python.org/pypi/fastcdc/)
[![Downloads](https://pepy.tech/badge/fastcdc)](https://pepy.tech/project/fastcdc)

This package implements the "FastCDC" content defined chunking algorithm in pure
Python. A critical aspect of its behavior is that it returns exactly the same
results for the same input. To learn more about content defined chunking and its
applications, see the reference material linked below.


## Requirements

* [Python](https://www.python.org/) Version 3.6 and later.

## Installing

```shell
$ pip3 install fastcdc
```

## Example Usage

An example can be found in the `examples` directory of the source repository,
which demonstrates reading files of arbitrary size into a memory-mapped buffer
and passing them through the chunker (and computing the SHA256 hash digest of
each chunk).

```shell
$ fastcdc -s 32768 tests/SekienAkashita.jpg
hash=5a80871bad4588c7278d39707fe68b8b174b1aa54c59169d3c2c72f1e16ef46d offset=0 size=32857
hash=13f6a4c6d42df2b76c138c13e86e1379c203445055c2b5f043a5f6c291fa520d offset=32857 size=16408
hash=0fe7305ba21a5a5ca9f89962c5a6f3e29cd3e2b36f00e565858e0012e5f8df36 offset=49265 size=60201
```

The  tests also have some short examples of using the chunker, of which this
code snippet is an example:

```python
from fastcdc import FastCDC

chunker = FastCDC.new("SekienAkashita.jpg", 16384, 32768, 65536)
results = [c for c in chunker]
assert len(results) == 3
assert results[0].offset == 0
assert results[0].length == 32857
assert results[1].offset == 32857
assert results[1].length == 16408
assert results[2].offset == 49265
assert results[2].length == 60201
```

## Reference Material

The algorithm is as described in "FastCDC: a Fast and Efficient Content-Defined
Chunking Approach for Data Deduplication"; see the
[paper](https://www.usenix.org/system/files/conference/atc16/atc16-paper-xia.pdf),
and
[presentation](https://www.usenix.org/sites/default/files/conference/protected-files/atc16_slides_xia.pdf)
for details. There are some minor differences, as described below.

### Differences with the FastCDC paper

The explanation below is copied from
[ronomon/deduplication](https://github.com/ronomon/deduplication) since this
codebase is little more than a translation of that implementation:

> The following optimizations and variations on FastCDC are involved in the chunking algorithm:
> * 31 bit integers to avoid 64 bit integers for the sake of the Javascript reference implementation.
> * A right shift instead of a left shift to remove the need for an additional modulus operator, which would otherwise have been necessary to prevent overflow.
> * Masks are no longer zero-padded since a right shift is used instead of a left shift.
> * A more adaptive threshold based on a combination of average and minimum chunk size (rather than just average chunk size) to decide the pivot point at which to switch masks. A larger minimum chunk size now switches from the strict mask to the eager mask earlier.
> * Masks use 1 bit of chunk size normalization instead of 2 bits of chunk size normalization.

The primary objective of this codebase was to have a Python implementation with a
permissive license, which could be used for new projects, without concern for
data parity with existing implementations.

## Prior Art

This crate is little more than a rewrite of the implementation by Joran Dirk
Greef (see the ronomon link below), in Rust, and greatly simplified in usage.
One significant difference is that the chunker in this crate does _not_
calculate a hash digest of the chunks.

* [nlfiedler/fastcdc-rs](https://github.com/nlfiedler/fastcdc-rs)
    + Rust implementation on which this code is based.
* [ronomon/deduplication](https://github.com/ronomon/deduplication)
    + C++ and JavaScript implementation on which the rust implementation is based.
* [rdedup_cdc at docs.rs](https://docs.rs/crate/rdedup-cdc/0.1.0/source/src/fastcdc.rs)
    + An alternative implementation of FastCDC to the one in this crate.
* [jrobhoward/quickcdc](https://github.com/jrobhoward/quickcdc)
    + Similar but slightly earlier algorithm by some of the same researchers.

## Change Log

## [1.0.0] - 2019-05-07

### Added
- Initial release (port of [nlfiedler/fastcdc-rs](https://github.com/nlfiedler/fastcdc-rs)). 

