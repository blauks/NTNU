#include "o3.h"
#include "gpio.h"
#include "systick.h"

/**************************************************************************//**
 * @brief Konverterer nummer til string 
 * Konverterer et nummer mellom 0 og 99 til string
 *****************************************************************************/
void int_to_string(char *timestamp, unsigned int offset, int i) {
    if (i > 99) {
        timestamp[offset]   = '9';
        timestamp[offset+1] = '9';
        return;
    }

    while (i > 0) {
	    if (i >= 10) {
		    i -= 10;
		    timestamp[offset]++;
		
	    } else {
		    timestamp[offset+1] = '0' + i;
		    i=0;
	    }
    }
}

/**************************************************************************//**
 * @brief Konverterer 3 tall til en timestamp-string
 * timestamp-argumentet mÃ¥ vÃ¦re et array med plass til (minst) 7 elementer.
 * Det kan deklareres i funksjonen som kaller som "char timestamp[7];"
 * Kallet blir dermed:
 * char timestamp[7];
 * time_to_string(timestamp, h, m, s);
 *****************************************************************************/
void time_to_string(char *timestamp, int h, int m, int s) {
    timestamp[0] = '0';
    timestamp[1] = '0';
    timestamp[2] = '0';
    timestamp[3] = '0';
    timestamp[4] = '0';
    timestamp[5] = '0';
    timestamp[6] = '\0';

    int_to_string(timestamp, 0, h);
    int_to_string(timestamp, 2, m);
    int_to_string(timestamp, 4, s);
}

//Hjelpende

#define LED_0_PIN 2
#define LED_PORT GPIO_PORT_E

#define BUTTON_PORT GPIO_PORT_B
#define BUTTON_0_PIN 9
#define BUTTON_1_PIN 10



volatile gpio_map_t * GPIO_map;
volatile sys_tick_map_t * SysTick_map;
volatile port_pin_t led0;
volatile port_pin_t button0;
volatile port_pin_t button1;

volatile int time[3];
volatile char timeString[7];

enum {STILL_SEKUNDER, STILL_MINUTTER, STILL_TIMER, TELL_NED, ALARM} state;

//Enable riktig MODE på riktig register på riktig pin

void enableGPIOregister(gpio_map_t * adress, port_pin_t * komp, byte mode){

	volatile word a;
	if (komp->pin > 7){
		a = adress->ports[komp->port].MODEH & ~(0b1111 << 4 * (komp->pin - 8));
		adress->ports[komp->port].MODEH = a| mode << 4 * (komp->pin - 8);
	}
	else{

		a = adress->ports[komp->port].MODEL & ~(0b1111 << 4 * komp->pin);

		adress->ports[komp->port].MODEL = a | mode << (4*komp->pin);


	}

}


//Enable interrupts på riktig pin og port
void enableGPIOinterrupt(gpio_map_t * adress, port_pin_t * button){
	/*
	 EXTIP er også delt i to: EXTIPSELH og EXTIPSELL, etter samme logik
	 som MODE registre (se seksjon 2.2.3);
	 */
	if (button->pin > 7){
				adress->EXTIPSELH &= ~(0b1111 << 4 * (button->pin - 8));
				adress->EXTIPSELH |= 1 << 4 * (button->pin - 8);
		}else{
				adress->EXTIPSELL &= ~(0b1111 << 4*button->pin);
				adress->EXTIPSELL |= 1 << 4*button->pin;
		}

	adress->EXTIFALL |= 0b1 << button->pin;
	adress->IFC |= 0b1 << button->pin;
	adress->IEN |= 0b1 << button->pin;


}

//Enable interrupts fra Systick

void enableSysTickInterrupt(sys_tick_map_t * adress){
	adress->CTRL |= 0b111;
	adress->LOAD = 14000000;
	adress->VAL = 0;
}

void SysTick_Handler(void){

	//GPIO_map ->ports[LED_PORT].DOUT ^= ((1<<LED_0_PIN));

	if(state == TELL_NED){
		if(time[0] == 0){
			time[0] = 59;
			if(time[1] == 0){
				time[1] = 59;
				time[2]--;
			}
			else{
				time[1]--;
			}
		}
		else{
			time[0]--;
		}

		if(time[0] == time[1] && time[1] == time[2] && time[2] == 0){
					state=ALARM;
					GPIO_map ->ports[LED_PORT].DOUTSET |= ((1<<LED_0_PIN));
				}
	}



}

void GPIO_ODD_IRQHandler(void){

	if(state <= STILL_MINUTTER){
		time[state]++;
		if(time[state] > 59){
			time[state] = 0;
		}
	}
	if(state == STILL_TIMER){
		time[state]++;

	}
	(*GPIO_map).IFC |= 0b1 << BUTTON_0_PIN;

}

void GPIO_EVEN_IRQHandler(void){

	if(state == ALARM){
		GPIO_map ->ports[LED_PORT].DOUTCLR ^= ((1<<LED_0_PIN));
		state = STILL_SEKUNDER;
	}
	else if(state <= STILL_TIMER){
		state++;
	}
	(*GPIO_map).IFC |= 0b1 << BUTTON_1_PIN;
}
int main(void) {
    init();

    GPIO_map = (gpio_map_t *)GPIO_BASE;

    SysTick_map = (sys_tick_map_t *)SYSTICK_BASE;

    led0.pin = LED_0_PIN;
    led0.port =LED_PORT;

    button0.port = BUTTON_PORT;
    button0.pin = BUTTON_0_PIN;

    button1.port = BUTTON_PORT;
    button1.pin = BUTTON_1_PIN;


    enableGPIOregister(GPIO_map,&led0,GPIO_MODE_OUTPUT);

    enableGPIOregister(GPIO_map,&button0,GPIO_MODE_INPUT);

    enableGPIOinterrupt(GPIO_map,&button0);

    enableGPIOregister(GPIO_map,&button1,GPIO_MODE_INPUT);

    enableGPIOinterrupt(GPIO_map,&button1);

    enableSysTickInterrupt(SysTick_map);

    time[0] = 0;
    time[1] = 0;
    time[2] = 0;

    state = STILL_SEKUNDER;
    while(true){

    	time_to_string(timeString,time[2],time[1],time[0]);

    	if(state == ALARM){
    		lcd_write("ALARM");
    	}
    	else{
    		lcd_write(timeString);
    	}

    }
    
    return 0	;
}

