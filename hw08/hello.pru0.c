#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
	int i;

	uint32_t *gpio3 = (uint32_t *)GPIO3;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	for(i=0; i<10; i++) {
		gpio3[GPIO_SETDATAOUT]   = P9_31;	// The the USR3 LED on
		__R30 |= P9_31;	

		__delay_cycles(500000000/5);    	// Wait 1/2 second

		gpio3[GPIO_CLEARDATAOUT] = P9_31;
		__R30 &= ~P9_31;	

		__delay_cycles(500000000/5); 

	}
	__halt();
}

// Turns off triggers
#pragma DATA_SECTION(init_pins, ".init_pins")
#pragma RETAIN(init_pins)
const char init_pins[] =  
	"/sys/class/gpio/export\0 110\0" \
	"/sys/class/gpio/gpio110/direction\0out\0" \
	"\0\0";