package com.learnMaven;

import static org.junit.Assert.assertNotEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

class simpleAppTest {
    @Test
    void rightReturnStatementTest(){
        // App app = new App();
        String exp_return  = "check out this return statement!";
        assertEquals(exp_return, App.main());
    }
    
    @Test
    void wrongReturnStatementTest(){
        String exp_return  = "WRONG";
        assertNotEquals(exp_return, App.main());   
    }
    
    @Test
    void trueReturnStatementTest(){
        assertTrue(App.main() instanceof String);   
    }
    
    // @Test  USE THIS WHEN YOUR METHOD SHOULD RETURN 'FALSE'
    // void falseReturnStatementTest(){
    //     assertFalse();    
    // }
    
    // @Test  USE THIS WHEN YOUR METHOD SHOULD RETURN NULL
    // void falseReturnStatementTest(){
    //     assertNull();    
    // }
    
    @Test
    void notNullReturnStatementTest(){
        assertNotNull(App.main());    
    }
    
    // @Test USE THIS WHEN YOUR METHOD SHOULD THROW AN EXCEPTION
    // void exceptionReturnStatementTest(){
    //     assertThrows(IllegalArgumentExcption.class,
    //     () -> {
    //         App.main(<illegalInput>);
    //     });
    // }
}