---
layout: post
title: HoloLens Video Streaming
---

There have been lots of discussion about streaming on HoloLens. Here is a demo of my implementation.

### Demo

<iframe width="100%" height="20rem" src="https://www.youtube.com/embed/RJ2GBQWfjvg" frameborder="0" allowfullscreen></iframe>

### Implementation

This application is implemented using the following toolset:

#### On PC

* Epiphan DVI2USB 3.0 and its SDK
* Python for `socket`, `queue`, and interfacing Epiphan SDK via `ctypes`
* Network connection

#### On HoloLens

* Made with Unity 5.5.0f3
* `Windows.Networking.Sockets.StreamSocket`
* [HoloToolkit](https://github.com/Microsoft/HoloToolkit-Unity)
* Network connection


The application runs at a reasonably frame rate and resolution (20fps with 896x594 resolution).


Thanks for reading! <img class="inline" src="/public/LQ144x144.png" alt="LQ" style="width:1.5rem;height:1.5rem;" />

