---
layout: post
title: ARToolKit on HoloLens
description: Demonstration of implementing ARToolKit on HoloLens. The capabilit of using the locatable camera of HoloLens to do fiducial marker tracking is exploited. 
tags: unity3d hololens hololens-artoolkit artoolkit vuforia marker-tracking
---

[HoloLens](https://www.microsoft.com/microsoft-hololens/en-us) is fascinating in terms of holographic display and in-room localization, but the capability of the front-facing camera ([locatable camera](https://developer.microsoft.com/en-us/windows/holographic/locatable_camera)) is not fully utilized for potential augmented reality applications.

### Why not Vuforia?

[Vuforia](https://vuforia.com/) released it support for HoloLens several month ago with Vuforia 6. Vuforia has its feature-based tracking, extended tracking mode, simple 3D model tracking, etc. However, there is several potential problems with Vuforia, from a developer point of view.

* Limited update rate, not intended for fast moving object.
* Lack of accuracy.
* Closed-source software, you have to get your finger-crossed for everything.
* Is charged.

### ARToolKit

Since [ARToolKit](http://artoolkit.org/) has served AR/VR for more than 10 years, and it is open-source, it would be nice to have it running on HoloLens. The obstacles towards this goal are quite clear as well:

* Universal Windows has a whole different set of tools and run-time libraries. The dependencies of existing ARToolKit does not exist on UWP, such as pthreads, video libraries, opencv.
* ARToolKit is written in native C/C++ code, and an additional wrapper is needed for development on Unity, which is recommended for HoloLens. (If you are not good at Direct3D, and Windows App)

**Luckily, after spending about a week on this, I successfully get some pieces of code written, and actually make ARToolKit runs on HoloLens, at about 40 fps.**

The repository is called [HoloLensARToolKit](https://github.com/qian256/HoloLensARToolKit) on Github.

### Demos

#### Samples of HoloLensARToolKit

There are three samples of HoloLensARToolKit, each representing a certain kind of marker that is supported: single marker, cube marker and multi marker.

<p class="full-width">
<iframe width="100%" style="height:24rem" src="https://www.youtube.com/embed/PqT90QfgP-U" frameborder="0" allowfullscreen></iframe>
</p>

#### Minion on the Cube

<p class="full-width">
<iframe width="100%" style="height:24rem" src="https://www.youtube.com/embed/cMzNyJkr3X0" frameborder="0" allowfullscreen></iframe>
</p>

This video is taken on HoloLens Device Portal, also known as **Mixed Reality Capture**. You might have noticed the lag between the video that is captured and update in the rendering. Because the tracking is able to complete within one rendering cycle, the lag is **probably** due to the post-rendering 3D warping of HoloLens.

#### More Screenshots

<span><table border=0><tr>
<td align="center" width="33%"><img src="http://longqian.me/public/image/artoolkit-hololens-single.png" /></td>
<td align="center" width="33%"><img src="http://longqian.me/public/image/artoolkit-hololens-cube.png" /></td>
<td align="center" width="33%"><img src="http://longqian.me/public/image/artoolkit-hololens-multi.png" /></td>
</tr><tr>
<td align="center">Single Marker</td>
<td align="center">Cube Marker</td>
<td align="center">Multi Marker</td>
</tr></table></span>

### Finally

You can access more articles describing the implementation details of [**HoloLensARToolKit**](https://github.com/qian256/HoloLensARToolKit) in my blog, simply clicking on the tag: <a class="no-underline" href="http://longqian.me/tag/hololens/"><code class="highligher-rouge"><nobr>hololens-artoolkit</nobr></code></a>.

With ARToolKit integrated with HoloLens, many more augmented reality applications are possible. If you are AR/VR developer, you must see what I mean here.

Thanks for reading. <img class="inline" src="/public/LQ144x144.png" alt="LQ" style="width:1.5rem;height:1.5rem;" />
