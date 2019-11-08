// GPIO base-adresse
GPIO_BASE = 0x40006000

// --- [Offset til GPIO-registrene]----------------------------------------- //
    // --- [Offset til portregistrene ] ------------------------------- //
        GPIO_PORT_CTRL     =  0     // Port Control Register
        GPIO_PORT_MODEL    =  4     // Port Pin Mode Low Register
        GPIO_PORT_MODEH    =  8     // Port Pin Mode High Register
        GPIO_PORT_DOUT     =  12    // Port Data Out Register
        GPIO_PORT_DOUTSET  =  16    // Port Data Out Set Register
        GPIO_PORT_DOUTCLR  =  20    // Port Data Out Clear Register
        GPIO_PORT_DOUTTGL  =  24    // Port Data Out Toggle Register
        GPIO_PORT_DIN      =  28    // Port Data In Register
        GPIO_PORT_PINLOCKN =  32    // Port Unlocked Pins Register
    // ---------------------------------------------------------------- //
    
    GPIO_EXTIPSELL  =  256  // External Interrupt Port Select Low Register
    GPIO_EXTIPSELH  =  260  // External Interrupt Port Select High Register
    GPIO_EXTIRISE   =  264  // External Interrupt Rising Edge Trigger Register 
    GPIO_EXTIFALL   =  268  // External Interrupt Falling Edge Trigger Register 
    GPIO_IEN        =  272  // Interrupt Enable Register 
    GPIO_IF         =  276  // Interrupt Flag Register 
    GPIO_IFS        =  280  // Interrupt Flag Set Register 
    GPIO_IFC        =  284  // Interrupt Flag Clear Register 

    GPIO_ROUTE      =  288  // I/O Routing Register 
    GPIO_INSENSE    =  292  // Input Sense Register 
    GPIO_LOCK       =  296  // Configuration Lock Register 
    GPIO_CTRL       =  300  // GPIO Control Register 
    GPIO_CMD        =  304  // EM4 Wake-up Clear Register 
    GPIO_EM4WUEN    =  308  // EM4 Wake-up Enable Register 
    GPIO_EM4WUPOL   =  312  // EM4 Wake-up Polarity Register 
    GPIO_EM4WUCAUSE =  316  // EM4 Wake-up Cause Register 
// ------------------------------------------------------------------------- //

// --- [Hjelpekonstanter til GPIO]------------------------------------------ //
    // Porter
    PORT_A          = 0
    PORT_B          = 1
    PORT_C          = 2
    PORT_D          = 3
    PORT_E          = 4
    PORT_F          = 5

    NUMBER_OF_PORTS = 6     // Antall porter
    PORT_SIZE       = 36    // Antall bytes i et sett med portregistre
    
    // Enheter på kitet
    LED_PORT        = PORT_E
    LED_PIN         = 2
    BUTTON_PORT     = PORT_B
    BUTTON_PIN      = 9
// ------------------------------------------------------------------------- //
