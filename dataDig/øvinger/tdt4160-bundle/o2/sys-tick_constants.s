// SysTick Base-addresse    
SYSTICK_BASE =  0xE000E010

// ---[ Offset til sys-tick-registrene ]------------------------ //
    SYSTICK_CTRL  = 0   // SysTick Control and Status Register
    SYSTICK_LOAD  = 4   // SysTick Reload Value Register
    SYSTICK_VAL   = 8   // SysTick Current Value Register
    SYSTICK_CALIB = 12  // SysTick Calibration Register
// ------------------------------------------------------------- //


// ---[ Hjelpekonstanter til sys-tick ]------------------------- //
    FREQUENCY = 14000000   // Antall klokkesignaler per sekund

    // CTRL-register-masker
    SysTick_CTRL_CLKSOURCE_Msk = 0b100
    SysTick_CTRL_TICKINT_Msk   = 0b010
    SysTick_CTRL_ENABLE_Msk    = 0b001
// ------------------------------------------------------------- //
