![librist logo](librist_logo.png)

# pyrist

Python binding for [librist](https://code.videolan.org/rist/librist)

This project is fully funded by [Mad Resistor LLP][https://madresistor.com/].

```
pip install rist
```

It will use system installed `librist.so` or `librist.dll` or use `LD_LIBRARY_PATH`.

## Goal and Features

The goal of this project is to provide an easy to use python interface over librist.

It supports all features of librist.

## Dependencies

* cffi
* enum

## License

**pyrist** is released under a very liberal license, a contrario from the other VideoLAN projects, so that it can be embedded anywhere, including non-open-source software; or even drivers, to allow the creation of hybrid decoders.

The reasoning behind this decision is the same as for libvorbis, see [RMS on vorbis](https://lwn.net/2001/0301/a/rms-ov-license.php3).

# Roadmap

The plan is the following:

### Reached
1. Working with librist.

### On-going
2. Write tutorials and comprehensive documentation.
3. Test on most platforms

# Contribute

Currently, we are looking for help from:
- Python developer
- testers.

Our contributions guidelines are quite strict. We want to build a coherent codebase to simplify maintenance and achieve the highest possible speed.

Notably, the codebase is in pure Python.

We are on Telegram, on the rist_users and librist_developers channels.

See the [contributions document](CONTRIBUTING.md).

## CLA

There is no CLA.

VideoLAN will only have the collective work rights.

## CoC

The [VideoLAN Code of Conduct](https://wiki.videolan.org/CoC) applies to this project.

# Install

```
python setup.py install
```

# Support

This project is fully funded by [Mad Resistor LLP][https://madresistor.com/].

This company can provide support and integration help, should you need it.


# FAQ

## Can I help?

- Yes. See the [contributions document](CONTRIBUTING.md).

## I am not a developer. Can I help?

- Yes. We need testers, bug reporters, and documentation writers.

## What about the packet recovery patents?

- This code was written to comply with the Video Services Forum (VSF) Technical Recommendations TR-06-1 and TR-06-2 and as such is free of any patent royalty payments

## Will you care about <my_arch>? <my_os>?

- Yes, as long as you can install Python and librist, you are good to go!

## How can I test it?

- You can use the `example/` code.
