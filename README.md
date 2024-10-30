# Overview #

Please review the license for use. 

This Project is still under development and not all features have been tested. As I work through the hardware I will continue to update. it is best to test this code will small actuators and another remote control unit prior to installing into an HY-550CJ. 

The HY-550CJ is a dangerous piece of equipment, any code that isn't tested should not be trusted as the machine is capable of serious injury to the user. In no way does the Authors or Contributors accept liability for damage to property or persons in use of this code or hardware. Care must be taken when using this repository. This same controller can be modified to fit other systems as it leverages the RC standard for control. It is best to test this on a safer piece of equipment (or remove the blades from the HY-550CJ prior to testing). 

This code is unable to control the output of the motors when the "Auto" Switch is open (in the off state). The Teensy outputs the power on its auto pin that then runs to the physical switch. This ensures that the device cannot override an operator's manual control. Unfortunately this switch must be located on the machine. 

[@ztokAutomates](https://www.youtube.com/@ztokautomates) will be covering safety of use of this equipment and hazards that operators, programmers, and contributors should be aware of prior to use.   

# Safety #

Do a risk assesment according to ISO 12100 to understand the risks. The following notes below are only a small subset of the most dangerous hazards associated with the machine.

* When working on the blades, disconnect the sparkplug to keep from unexpected engine startup.
* Never place yourself inbetween the machine and a fixed object. The crushing hazard is the one of the most dangerous hazards assocated with the base (not including the blades)
* It is possible to get entangled into the machine tracks, make sure to power off the machine and controller before working on the tracks. Do not underestimate the power and speed of unexpected movement.
* Do Not Ride the Machine. It does have enough power to move people on it but with all of the risks of the tracks, blades, and engine; there is no safe way to ride it. If the intent is to ride the machine then add that task to the risk assesment to understand what hazards you will need to protect from (including rollover).
* When doing the risk assesment ensure to take into account bystandards that will not know about any of these risks (people assume machines are safe and are not hazardous). It is the operator's reponsibilty to keep people safe and understand the hazards assocated with the machine (this is typically accomplished with signs).
* Only use the charger that came with the machine. The port on the machine to charge it is a standard IEC Plug used on 120VAC systems. This Plug on the equpment is actually a 12VDC circuit and plugging it into the wall can cause the frame to be engergized and destroy the control system within the machine and can lead to fire.
* This machine has not been evaluated by any NRTLs (Nationally Recoginized Testing Labratories, like NSF or UL). It is possible (although unlikely) that this system may catch fire if care is not taken.
* There is no rollover cutoff on the machine. if the machine rolls over it will damage the engine. Climbing hills can also damage the engine if constantly doing hills. Give the machine a break if doing a lot of hills. [Video Snipit](https://www.youtube.com/watch?v=2dOWbkyhdJA&t=2900s)
* There is a possibily of debris being ejected from under the machine, wear protective equipment when operating it. The most dangerous places to be are infront and behind the equipment. It can also be ejected from the sides. [It has reached over 10ft in my experience (standing behing it)](https://www.youtube.com/watch?v=2dOWbkyhdJA&t=3720s). Be mindeful of this when operating it.

## Limits ##
* Maximum flat pull force > 300 lbsf (the belts do not stop at this force)
* Maximum speed < ~ 300mm/s (1 ft/s)
* Maximum climb angle < 45 degrees in the forward direction.  

# Setup #
* The Teensy needs to be setup to disable being powered from the USB port to enable debugging under power. [Teensy Reference](https://www.pjrc.com/teensy/external_power.html)
* J1 on the board links the Board 5Vdc to the Motor and Input 5Vdc to power the controller and smaller motors. it should not be used when in the HY-550CJ since power comes from the motor controllers.

# Parts #
 
 [Mouser Project](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=017e74ae19)

 Teensy4.1 and GPS boards (2x for robot, 1x for base station) are seperate.
 [GPS Board](https://www.sparkfun.com/products/16481)

 Headers and Sockets included for Teensy and GPS boards.

 [HY-550CJ](https://www.alibaba.com/product-detail/FREE-SHIPPING-CE-EPA-Remote-Control_1600909334029.html?spm=a2700.galleryofferlist.normal_offer.d_title.51b313a0xlqezM)

 [Base Station Radio 100mW 915Mhz](https://holybro.com/products/sik-telemetry-radio-v3?variant=41562952302781)
