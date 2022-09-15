# Purple Owl

<p align="center" width="100%">
    <img width="25%" src="assets/purple-owl-logo.png">
</p>

The Purple Owl is a uniform row staggered 60% keyboard designed around ortholinear 1u keycaps and hotswap sockets.

## Layout
The Purple Owl was inspired off the works of Ziptyze with their Zlant (4x12) and ZlantXL (5x12). It is almost like a staggered 5-row Preonic but with more columns a narrow bottom row to offer the visual aesthetic of four dominant rows like a Plank. Each row has a 0.25u stagger unlike a traditional row-stagger. There are 14 columns to accommodate the outer symbols (`-=[]\`). The right shift can be traded in for an arrow cluster. The ctrl, shift and other mods are designed to be under the thumbs with a symmetric bottom row that has a 2u surrounded by two 1u on each side. The board runs on [KMK](http://kmkfw.io/), so the keys can be freely mapped.

<p align="center" width="100%">
    <img width="75%" src="assets/purple-owl-kle.png">
</p>

Link to the base layout at [Keyboard Layout Editor](http://www.keyboard-layout-editor.com/#/gists/7c51d0df5eb78da5dd614ee6019f13bc). KLE Raw is also available [here](purple-owl-kle.txt)

## Electronics
Instead of a traditional diode matrix, the Purple Owl implements a **scan chain** to poll the state of its switches using only 3 logic pins. This opens the door to support a wide variety of off-the-shelf microcontrollers including the Pro Micro layout variants popular in the mechanical keyboard community. KMK supports a scan chain scanner by default. So, any CircuitPython compatible board with the pinouts shown below should snap into Purple Owl. There is a solder jumper to select between two popular layouts - the Pro Micro variant and the Seeed XIAO variant. The Purple Owl design needs two power pins (3V3 and GND) and three logic pins (CLK, DATA, LATCH).

<p align="center" width="100%">
    <img width="75%" src="assets/pinout.jpeg">
</p>

> While, I currently have a bunch of RP2040 boards in various layouts, I eventually might test out KMK BLE wireless with some CircuitPython compatible nrf52840 board like the nice!nano, [Seeed nrf52840](https://www.seeedstudio.com/Seeed-XIAO-BLE-Sense-nRF52840-p-5253.html) or Adafruit QTPy Bluefruit (doesn't exist yet?). Anything with a JST connector for the battery.

## Seeed XIAO Mechanical Keyboard Contest
I came across an article for this [contest](https://www.seeedstudio.com/seeed-fusion-diy-xiao-mechanical-keyboard-contest.html) on [KBD.news](https://kbd.news/). The Purple Owl was designed to be powered by a [Seeed XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html) (or any CircuitPython compatible Seeed XIAO for that matter) and will be my entry in the contest! Seeed is sponsoring two fully [assembled PCBs](https://www.seeedstudio.com/pcb-assembly.html) - and that is an opportunity I simply couldn't pass on.

<p align="center" width="75%">
    <img src="assets/purple-owl-1p0-3D-top.png">
</p>

The tiny size of the Seeed XIAO RP2040 will be perfect to highlight the GPIO-efficient scan-chain design. Aside from the 61 switches, the Seeed XIAO RP2040 will drive 16 underglow LEDs which will look stunning in a laser cut case.

## News
- The prototype appeared on KBD.news! [Link](https://kbd.news/Purple-Owl-1581.html)

## Gallery

<p align="center" width="100%">
    <img src="assets/photos/dark0.jpg">
</p>
<p align="center" width="100%">
    <img src="assets/photos/dark1.jpg">
</p>
<p align="center" width="100%">
    <img src="assets/photos/dark2.jpg">
</p>

## PCB
![done](https://img.shields.io/badge/Work-Complete-green?style=for-the-badge&logo=github)

### Externals
- Acheron MX footprints ([link](https://github.com/AcheronProject/acheron_MXH.pretty.git)) for Kailh hotswap sockets.
- Geometric animals art for the silkscreen ([link](https://www.etsy.com/listing/873524342/geometric-animals-bundle-svg-linear]))
- JLCPCB Tools for Kicad ([link](https://github.com/Bouni/kicad-jlcpcb-tools)) to generate the gerbers and assembly files for JLCPCB.

### Prototype v0.1
To get a feel for the layout I prototyped a board that runs off a RP2040 microcontroller, the Waveshare RP2040 Zero. When I started the prototype, I intended for the the final Purple Owl PCB to have all electronics integrated on the board, including the RP2040. The prototype PCB is simply a diode matrix of hotswap sockets and diodes hooked up to the Zero. No LEDs or anything fancy yet.

I referred to the "recommended minimums" on [Acheron Setup](http://acheronproject.com/acheron_setup/acheron_setup/) for board rules which are more constrained for some fields that the default JLCPCB setup. Laying out the switches is a cakewalk once you set the grid to 19.05mm (1u or 0.75in). For the stagger, set the grid to 4.7625mm (0.25u or 19.05/4mm). The controller is tilted by 26' which is along the ~~z~~slant of the columns.

<p align="center" width="100%">
    <img src="assets/purple-owl-prototype.png">
</p>

I checked for clearance pretty early on as soon as I had the swtiches and controller laid out to make sure the slightly tilted controller and USB cable seemed ok on the right side. I printed half(~ish) the layout flipped on paper to scale.

<p align="center" width="100%">
    <img width="50%" src="assets/prototype_clearance_check.jpg">
</p>

For assembly, I wanted to trial JLCPCB's assembly service - especially for hotswap sockets. While, I could simply solder the sockets myself, I was curious about JLCPCB's work. And, if it did work, then building the proper Purple Owl would be fairly turnkey.

The footprint for the JLCPCB [part](https://jlcpcb.com/partdetail/Kailh-CPG151101S11/C2803348) for the Kailh hotswap socket is centered around the socket itself. But, the switch footprint on the PCB is centered around the stem hole. So, I wrote a [small python snippet](pcb/tools/fix_pos.py) to fix the socket position and rotation in the POS assembly file. Below, you can see how it looks before (right) and after (left) the fix on the JLCPCB assembly preview.

<p align="center" width="100%">
    <img width="35%" src="assets/jlcpcb_fix_pos.png">
</p>

The cost for the PCB fabrication and assembly came up to $85 for 5 boards assembled. The 305 hotswap sockets (61 per board) going at 78 cents a piece for a total of about $24. In hindsight, I should have just assembled 2 boards considering this was a prototype, but my excitement got the better of me.

> Firmware Note: The Zero supports CircuitPython and thus, KMK. So, not much work to be done aside from the KMK config for the matrix. I'd need to add CircuitPython support for the RP2040 layout integrated on the proper Purple Owl (if I went that route), but that seems easy looking at [how it was ported](https://sourcegraph.com/github.com/adafruit/circuitpython/-/tree/ports/raspberrypi/boards/waveshare_rp2040_zero) for the Zero.

### Revelation: The Scan Chain

A while back, I had considered shift registers for scanning the switch matrix in passing when I had read this [Hackaday article](https://hackaday.com/2018/09/30/whats-the-cheapest-way-to-scan-lots-of-buttons/). Along the lines of using 2 shift registers for an 8x8 matrix - one serial-to-parallel to drive the columns and a parallel-to-serial to poll the rows. While this would use only two 8-bit shift registers, I'd still need diodes per switch for NKRO. However, I'd need no more than 5-6 pins to interface with the switch matrix over the two shift registers. At first glance, the approach didn't really seem any better than using a traditional diode matrix and routing the columns and rows to the IOs of the microcontroller (especially since I was considering integrating the RP2040 on the board).

Then, I stumbled upon an article for the [Hello World Smart Keyboard](https://kbd.news/Hello-Word-Smart-Keyboard-1569.html) project when Dovenyi posted their [#89 issue of the KBD News Digest](https://www.reddit.com/r/MechanicalKeyboards/comments/wdgbuy/keyboard_builders_digest_issue_89/) on r/mk. It was a curiously interesting design with 74HC165 shift registers polling _all_ switches latched in parallel along a 1xN matrix. Surely, this would need a lot of shift registers (one IC per 8 keys) and pull up resistors per switch. So, in terms of parts, the design used relatively more parts (and proper active components). Nonetheless, the most attractive part of the design was that it needed merely 3 pins to interface with the matrix.

While I was running a embarrassingly one-sided rubber ducking session with Dovenyi on that reddit thread, I realized something. Using fewer fins suddenly opens up a design where I can attach off-the-shelf (OTS) microcontroller boards right in between the switches (alongside the hotswap sockets) - underneath the switches and not on the side. Because, I'd only need to solder enough headers for functional and mechanical purpose. I could use something tiny like a [Adafruit QTPy RP2040](https://www.adafruit.com/product/4900) or [Pimoroni Tiny RP2040](https://shop.pimoroni.com/products/tiny-2040?variant=39560012234835) and merely use just one side of the pins between the sockets, and some on the other side for mechanical stability.

These uC (microcontroller) boards are typically 700mil wide with their columns of pins 600mil apart. They don't fit around hotswap sockets if you are using all the pins. It does work for soldered switch footprints like in the case of ErgoDash or ErgoTravel, but not for hotswap sockets because of the wider footprint. Hence, in the prototype I had the uC on the side. Secondly, the uC boards that have enough pins for a diode matrix are typically longer than 1U and won't fit across the rows of a row-staggered layout (while they do work for ortho or column staggered layouts). Now, these problems are washed out when you realize that you don't need to drill and solder headers for _all_ the pins. Just enough to get the job done. And, you don't really need to use a small board like the QTPy. Even a KB2040 would work - since you don't have to drill holes across the rows to access all the pins.

I had almost gone down the path of designing an integrated RP2040 board. Researched a bunch of popular designs and minimal RP2040 circuits, and printed all their schematics. I had even picked out the parts on LCSC and had calculated the trace widths and separation required for the differential pair routing for the USB Full Speed mode (90ohm Z_diff). Because I didn't think there was a _good_ design I where I could have the uC board underneath and not on the side...

And now, there was a way.

> Firmware Note: Looks like KMK has a scanner for shift registers ([see](https://github.com/KMKfw/kmk_firmware/blob/master/kmk/scanners/keypad.py)) that wraps CircuitPython's `keypad.ShiftRegisterKeys()`. Great!

### Production v1.0
The design uses 8 74HC165 (TSSOP-16 package) to form the scan chain. 7 of these poll the top 4 rows across 14 columns and the last one polls the bottom row. I've also added 16 underglow LEDs (WS2812B-V5). Compared to the prototype, the design now has a clean board edge tightly fitting the switches, since the uC now goes underneath. The uC is socketed to the board with through-hole headers. Out of the 14 pins of the Seeed XIAO RP2040, 11 are connected.

<p align="center" width="100%">
    <img src="assets/purple-owl-1p0-pcb.png">
</p>

There are jumpers to select the 3V3 source depending on the attached uC. And jumpers to select the power source (3.3V or 5V) for the LEDs. Though off-spec, The LEDs work fine on 3.3V, albeit slightly less bright than if powered by 5V. There wasn't enough space (while staying close to the board edge) to allow a through hole header for the 5V, so the design offers a jumper/through-hole that needs to be wired between the board and the jumper site if 5V is desired.

- JP1: Join `1-2` or `2-3` depending on where the 3V3 pin on the uC is. For the Seeed XIAO RP2040 variants short the `1-2`. And, for Pro Micro variants, short `2-3`.
- JP2: Join `1-2` to select the 3.3V source selected by JP1, or connect the 5V to `3` from the uC over a wire and join `2-3`.

For assembly, Seeed is sponsoring two fully assembled boards 🎉

<p align="center" width="100%">
    <img width="50%" src="assets/photos/pcb_mounting.jpg">
</p>

## Firmware

This project was my first experience with CircuitPython, let alone KMK. I am stunned how wasy it was to work with. Never did I think it would take just few lines of python to establish a fully functional keyboard with layers and underglow LEDs.

There are bringup scripts for the both PCB variants which test the PCB and demonstrate interfacing with the keyboard switches using native CircuitPython.
- [v0.1 bringup](firmware/v0.1/bringup.py) - diode matrix.
- [v1.0 bringup](firmware/v1.0/bringup.py) - scan chain. Using digitalio, it took about 1ms to scan 61 switches. 

The [setup](firmware/v0.1/main.py) for the prototype v0.1 diode matrix was fairly straightforward with KMK. I included three basic layers to start with (I really need the tilde/grave in my line of work). The physical layout of the switches were mapped to the layout with the `coord_mapping` setup.

The [build](firmware/v1.0/main.py) for the v1.0 PCB inherited the same layers. The firmware switched the `scanner` to the `ShiftRegisterKeys()` and updated the `coord_mapping` to the physical layout of the scan chain. KMK offeres a neat `RGB` extension to support the underglow LEDs. The underglow RGB controls are added on a layer. Looking at the sheer simplicity of the [RGB extension](https://github.com/KMKfw/kmk_firmware/blob/master/kmk/extensions/rgb.py) I might consider writing a fancy underglow mode or two. Since, this was a *proper* build, the [`boot.py`](firmware/v1.0/boot.py) was updated with a "dev mode" which hides CircuitPython enumerations (serial, midi and storage) except for the USB HID keyboard.

## Credits
- Layout inspired by Ziptyze's [Zlant](https://1upkeyboards.com/shop/keyboard-kits/diy-40-kits/zlant-40-acrylic-keyboard-kit/) and [ZlantXL](https://1upkeyboards.com/shop/keyboard-kits/diy-40-kits/zlantxl-50-mechanical-keyboard-kit/).
- Electronics inspired by Zhihui's [HanWen](https://github.com/peng-zhihui/HelloWord-Keyboard) and Tzarc's [Ghoul](https://github.com/tzarc/ghoul) which use shift registers to scan the matrix.
- Dovenyi and [Keyboard Builder's Digest](https://kbd.news/).
- Seeed DIY XIAO Mechanical Keyboard Contest, [Link](https://www.seeedstudio.com/seeed-fusion-diy-xiao-mechanical-keyboard-contest.html).

## Why
I have a gorgeous looking ortho keycap set, MT3 Cyber lying around and it was a shame to not have adorned on a board. I also loved the feel of a shift and ctrl under my left thumb like my setup on the Iris v6, a split column-staggered layout. But, I missed my arrows keys and outer column symbols (which were on a layer). Once, I saw the Zlant - I simply knew I had to make the Purple Owl. Plus, it's been a over a year since I designed a PCB, or worked on a [hobby electronics project](https://github.com/SonalPinto/krz-arduboy2) and wanted to get into something before I forget how to DIY.
