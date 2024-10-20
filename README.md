# Overview #
This Project is still under development and not all features have been tested. As I work through the hardware I will continue to update. it is best to test this code will small actuators and another remote control unit prior to installing into an HY-550CJ. The HY-550CJ is a dangerous piece of equipment, any code that isn't tested should not be trusted as the machine is capable of serious injury to the user. In no way does the Authors or Contributors accept liability for damage to property or persons in use of this code. Care must be taken when using this code. This same controller can be modified to fit other systems as it leverages the RC standard for control. It is best to test this on a safer piece of equipment (or remove the blades from the HY-550CJ prior to testing). 

This code is unable to control the output of the motors when the "Auto" Switch is open (in the off state). The Teensy outputs the power on its auto pin that then runs to the physical switch. This ensures that the device cannot override an operator's manual control. Unfortunately this switch must be located on the machine. 

[@ztokAutomates](https://www.youtube.com/@ztokautomates) will be covering safety of use of this equipment and hazards that operators, programmers, and contributors should be aware of prior to use.   

# Parts #
 
 [Mouser Project](https://www.mouser.com/ProjectManager/ProjectDetail.aspx?AccessID=017e74ae19)

 Teensy4.1 and GPS boards (2x) are seperate.
 [GPS Board](https://www.sparkfun.com/products/16481)

 Headers and Sockets included for Teensy and GPS boards.

 [HY-550CJ](https://www.alibaba.com/product-detail/FREE-SHIPPING-CE-EPA-Remote-Control_1600909334029.html?spm=a2700.galleryofferlist.normal_offer.d_title.51b313a0xlqezM)
