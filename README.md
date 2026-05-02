```bash
$ cat harinandan.profile
# -----------------------------------------------
# Name    : Harinandan J V
# Alias   : awesomesno
# Age     : 18
# Loc     : Kerala, India
# Orgs    : AxeomLabs  |  The Shadow Company
# URL     : harinandan.in
# Status  : Debugging 6 impossible projects at 2am
# -----------------------------------------------
# Recent activity:
#   Wrote a bootloader         [done]
#   Built an x64 CPU emulator  [done]
#   Started a game engine      [in progress, send help]
#   Automated my house         [done, it works, mostly]
#   Built a physics simulator  [objects make sounds now. yes on purpose]
#   Writing an OS from scratch [you read that right]
# -----------------------------------------------
$
```

<br>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=32&duration=3500&pause=99999&color=39FF14&center=true&vCenter=true&repeat=false&width=500&lines=hi.+i'm+harinandan." />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=3500&pause=99999&color=39FF14&center=true&vCenter=true&repeat=false&width=828&lines=I%27m+18+year+old+from+Kerala+who+thought+%22building+an+OS+from+scratch%22+was+a+reasonable+thing+to+do" />
</p>

<br>

<p align="center">
  <img src="https://img.shields.io/badge/age-18-39FF14?style=flat-square&labelColor=0d0d0d" />
  <img src="https://img.shields.io/badge/location-Kerala%2C_India-39FF14?style=flat-square&labelColor=0d0d0d" />
  <img src="https://img.shields.io/badge/sleep_schedule-what's_that%3F-ff4444?style=flat-square&labelColor=0d0d0d" />
  <img src="https://img.shields.io/badge/status-building_too_many_things-39FF14?style=flat-square&labelColor=0d0d0d" />
  <img src="https://komarev.com/ghpvc/?username=AwesomeSno&label=people+who+ended+up+here&color=39FF14&style=flat-square&labelColor=0d0d0d" />
</p>

---

## Ok so here's the deal

I'm self-taught. No cs degree, no bootcamp, no roadmap. I just started building things that seemed too hard and kept going until they weren't.

I write operating systems from bare metal, binary translators for x64 executables, game engines from scratch, physics simulators, smart home automation systems, and apparently also robotic arms that respond to hand gestures. Not for work. Just because I want to understand how everything works at the lowest possible level. If I can't build it from scratch, I don't feel like I really understand it.

I run **AxeomLabs** (proprietary systems, research-grade software) and **The Shadow Company** (a tech collective for people who actually build things). Both are real. Both are active. Both have more going on than is public right now.

---

## What I'm actually building rn

> Not "what I'm interested in." What I am literally working on right now.

<table>
<tr>
<td width="50%" valign="top">

### 🖥️ Untitled OS
`C` `Assembly` `bare metal` `in dev`

An operating system built from bare metal. No Linux base, no borrowed kernel, no shortcuts. Custom bootloader, memory manager, scheduler, the whole thing. The goal is an OS where privacy isn't a setting you toggle, it's just how the system works by design.

Yes I know how that sounds. Yes I'm still doing it. (No name yet. It'll get one when it deserves one.)

</td>
<td width="50%" valign="top">

### 🎮 Project Engine
`C++20/23` `AxeomLabs` `proprietary`

A unified game engine AND scientific simulation platform in one codebase. Seven major subsystems. Targets nine platforms including consoles. One of those subsystems is a biomechanics engine with actual Hill-type muscle models and injury simulation. Yeah. I'm also pulling in parts of Godot for faster development on certain areas so I don't burn time reinventing things that are already solid. The core architecture is still mine.

This one's going to take a while but I'm not cutting corners on any of it.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🪟 ProWin
`C++` `Swift` `open source` `v0.15.0`

Loads and runs Windows x64 PE32+ binaries directly on macOS. No VM. I wrote the dynamic binary translator myself. Translates DirectX to Metal, XAudio2 to AVFoundation, XInput to GameController in real time.

Currently handles simple binaries correctly. DirectX pipeline is next. I'm also thinking about pulling in parts of Wine for some of the compatibility layer work, though that's not a final decision yet. Long road but it works.

</td>
<td width="50%" valign="top">

### ⚡ Zero Invasion
`C++20` `pre-alpha`

Real-time 2D/3D physics simulation platform. Rigid bodies, soft bodies, joints, materials, wind, gravity. The part nobody else does: every object emits sound based on its material, velocity, and collision force. Physics-driven audio synthesis. In real time.

Runs natively on Metal, Vulkan, and OpenGL. There's a chance this gets absorbed into Project Engine as a subsystem down the line. Nothing decided yet.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔐 ZeroVault
`privacy app` `in dev`

Encrypted notes app. No cloud, no sync, no accounts, no telemetry, nothing leaves your device. Ever. Made it because I wanted a notes app that actually means it when it says local-only and not "local unless we decide otherwise."

</td>
<td width="50%" valign="top">

### 🏠 Home Automation System
`ESP32` `prototyped`

Whole-house automation with lighting, security, environmental monitoring, and access control. No SmartThings, no Alexa, no subscription, no cloud. Just hardware I wired and code I wrote.

</td>
</tr>
</table>

<details>
<summary><b>There's one more (click if you're curious)</b></summary>

<br>

### 🤖 Robotic Arm
`Arduino` `OpenCV` `prototyped`

3D-printed robotic arm that mirrors my hand in real time using OpenCV-based hand gesture recognition. Working on a custom controller UI separately but that's on hold for now, got bigger things going on.

The gesture control is the cool part anyway.

<br>
</details>

---

## the honest checklist

```
DONE:
[x]  written a bootloader in assembly
[x]  built a working x64 CPU emulator from scratch
[x]  designed a 7-module cross-platform game engine architecture
[x]  automated an entire house with custom ESP32 code
[x]  made a robotic arm respond to hand gestures via computer vision
[x]  built a physics sim where objects generate sound from their material
[x]  shipped an encrypted notes app with zero external dependencies
[x]  started a proprietary software lab  (AxeomLabs)
[x]  started a tech collective           (The Shadow Company)

STILL COOKING:
[ ]  Untitled OS first boot                   // getting there
[ ]  Project Engine running a game            // it's a marathon
[ ]  ProWin running a full DirectX title      // making real progress
[ ]  Zero Invasion v1.0 public release        // steady
[ ]  sleep a normal amount                    // not looking good honestly
```

---

## Stuff I know

```
languages    C  |  C++  |  C#  |  Assembly  |  Python  |  Swift  |  Bash  |  HTML/CSS

gpu apis     Metal  |  Vulkan  |  OpenGL  |  DirectX 12

tools        CMake  |  Ninja  |  Xcode  |  Make  |  Git

frameworks   OpenCV  |  Unreal Engine  |  Unity  |  SwiftUI  |  Dear ImGui  |  JoltPhysics

hardware     Arduino  |  ESP32  |  3D printing

domains      OS development       |  binary emulation       |  systems programming
             computer vision      |  embedded systems       |  game engine architecture
             cybersecurity        |  robotics               |  physics simulation
             AI + ML              |  real-time audio        |  networking
```

---

## Proof I exist and actually commit

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=AwesomeSno&show_icons=true&hide_border=true&count_private=true&include_all_commits=true&bg_color=0d0d0d&title_color=39FF14&icon_color=39FF14&text_color=777777" width="49%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=AwesomeSno&layout=compact&hide_border=true&bg_color=0d0d0d&title_color=39FF14&text_color=777777" width="49%" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=AwesomeSno&hide_border=true&ring=39FF14&fire=39FF14&currStreakLabel=39FF14&background=0d0d0d&sideLabels=ffffff&dates=dddddd&currStreakNum=ffffff&sideNums=ffffff" width="65%" />
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=AwesomeSno&bg_color=0d0d0d&color=39FF14&line=39FF14&point=ffffff&area=true&area_color=0d0d0d&hide_border=true" width="95%" />
</p>

---

## One thing I actually believe

> *"If you don't understand how it works at the lowest level, you don't really understand it."*

Most people wait until they're "ready" to start something hard. I don't think that ever comes. So I just start, go learn what I'm missing, and come back. That's how you end up writing bootloaders at 17 and not thinking it's weird.

---

## find me

<p align="center">
  <a href="https://harinandan.in">
    <img src="https://img.shields.io/badge/harinandan.in-website-39FF14?style=for-the-badge&logo=googlechrome&logoColor=black&labelColor=0d0d0d" />
  </a>
  <a href="https://in.linkedin.com/in/snox">
    <img src="https://img.shields.io/badge/snox-linkedin-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0d0d0d" />
  </a>
  <a href="https://instagram.com/snozuuz">
    <img src="https://img.shields.io/badge/snozuuz-instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white&labelColor=0d0d0d" />
  </a>
  <a href="mailto:harinandanjv@gmail.com">
    <img src="https://img.shields.io/badge/harinandanjv@gmail.com-email-ff4444?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0d0d0d" />
  </a>
</p>

---

<br>

<p align="center">
  <sub>If you want to build something genuinely ambitious, you know where to find me.</sub><br><br>
  <sub>If something here seems impossible for a 18 year old -- that's exactly why I'm doing it.</sub>
</p>
