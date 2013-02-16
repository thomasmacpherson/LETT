#! /usr/bin/python

# A simple Python command line tool to control an MCP23017 I2C IO Expander
# By Nathan Chantrell http://nathan.chantrell.net
# GNU GPL V3 

# SK Pang Electronics June 2012

import smbus
import sys
import getopt
import time 
import const
bus = smbus.SMBus(0)

address = 0x10 # I2C address of MCP23017
bus.write_byte_data(0x20,0x00,0x00) # Set all of bank A to outputs 
bus.write_byte_data(0x20,0x01,0x00) # Set all of bank B to outputs 


const.MAX_WIRE_CMD  =        0x80

const.CMD_NOP       =        0x00

const.CMD_SWAP_BUF  =        0x10
const.CMD_COPY_FRONT_BUF =   0x11
const.CMD_SHOW_AUX_BUF   =   0x12

const.CMD_CLEAR_BUF       =  0x20
const.CMD_SET_PAPER       =  0x21
const.CMD_SET_INK         =  0x22
const.CMD_CLEAR_PAPER     =  0x25
const.CMD_DRAW_PIXEL    =    0x26
const.CMD_DRAW_LINE     =    0x27
const.CMD_DRAW_SQUARE    =   0x28
const.CMD_PRINT_CHAR     =   0x2A
const.CMD_DRAW_ROW_MASK  =   0x2B
const.CMD_SET_BOARD_BG   =   0x2C
const.CMD_SET_BOARD_SIZE =   0x2D
const.CMD_MOVE_UNTIl     =   0x2E
const.CMD_CLEAR_SPACE     =  0x2F

unsigned char CMD_totalArgs[MAX_WIRE_CMD] = [
#  0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - A - B - C - D - E - F 
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 0 - 0x00 -> 0x0F
    0,  2,  1,  2,  1,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,    # 1 - 0x10 -> 0x1F
    3,  3,  3,  0,  0,  0,  2,  4,  4,  0,  3,  3,  6,  1,  5,  2,    # 2 - 0x00 -> 0x2F
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 3 - 0x00 -> 0x3F
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 4 - 0x00 -> 0x4F
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 5 - 0x50 -> 0x5F
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,    # 6 - 0x60 -> 0x6F
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0     # 7 - 0x70 -> 0x7F
# 0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - A - B - C - D - E - F 
];









unsigned char RainbowCMD[20];

void setup()
{
  Wire.begin(); // Start I2C Bus as Master

  RainbowCMD[0] = 'r';

}
void loop()
{
  delay(500);
    sendCMD(remoteAddr,CMD_SET_BOARD_SIZE, toByte(4));
  //sendCMD(remoteAddr, CMD_SET_BOARD_BG,random(0xF),random(0xF),random(0xF),random(0xF),random(0xF),random(0xF));
  delay(500);
  sendCMD(remoteAddr, CMD_SET_INK, 0xF, 0x0, 0xF);
    //Serial.println(toByte(4));
    
    
  delay(1000);
  sendCMD(remoteAddr, CMD_MOVE_UNTIl,  toByte(0), toByte(0), toByte(3), toByte(3),toByte(100));
  delay(2000000);
  sendCMD(remoteAddr, CMD_DRAW_PIXEL,toByte(4),toByte(5));
  delay(1000);
  sendCMD(remoteAddr, CMD_CLEAR_SPACE,toByte(4),toByte(5));
  delay(1000);
  sendCMD(remoteAddr,CMD_SET_BOARD_SIZE, toByte(4));

  //sendCMD(remoteAddr, CMD_DRAW_SQUARE, toByte(0), toByte(0), toByte(8), toByte(8));

  delay(1500);
  sendCMD(remoteAddr, CMD_SET_BOARD_BG,random(0xF),random(0xF),random(0xF),random(0xF),random(0xF),random(0xF));
  //sendCMD(remoteAddr2, CMD_SET_INK, 0x0, 0xFF, 0x0);
  //sendCMD(remoteAddr2, CMD_DRAW_LINE,  toByte(2), toByte(2), toByte(6), toByte(6));
  delay(500);
  sendCMD(remoteAddr, CMD_SET_INK, 0xF, 0xF, 0xF);
    //Serial.println(toByte(4));
    
    
  delay(1000);
  sendCMD(remoteAddr, CMD_DRAW_PIXEL,toByte(0),toByte(1));
  delay(1000);
  sendCMD(remoteAddr, CMD_CLEAR_SPACE,toByte(0),toByte(1));
  delay(500);
 
  //sendCMD(remoteAddr, CMD_SET_INK, 0x0, 0x0, 0xFF);
 // sendCMD(remoteAddr, CMD_DRAW_LINE,  toByte(2), toByte(2), toByte(7), toByte(7));
 
  /*
  Wire.beginTransmission(remoteAddr); // transmit to device #9
  Wire.write(random(8));              // sends x
  Wire.write(random(8)); 
  Wire.endTransmission();    // stop transmitting
  x++;
  if (x > 5) x=0;
  */
  delay(100000);
}



















def sendCMD(byte address, byte CMD, ... ):
  int i;
  unsigned char v;
  byte t;
  va_list args;                     # Create a variable argument list
  va_start(args, CMD);              # Initialize the list using the pointer of the variable next to CMD;
  
  RainbowCMD[1] = CMD;              # Stores the command name
  t = pgm_read_byte(&(CMD_totalArgs[CMD]))+2;  # Retrieve the number of arguments for the command
  for (i=2; i < t; i++) {
    v = va_arg(args, int);          # Retrieve the argument from the va_list    
    RainbowCMD[i] = v;              # Store the argument
  }
  
  sendWireCommand(address, t);      # Transmit the command via I2C
}

unsigned char toByte(int i) {
  return map(i, -128, 127, 0, 255);
}

 ### The following lines are adapted from the original code ###

def sendWireCommand(int Add, byte len):
  unsigned char OK=0;
  unsigned char i,temp;
  Wire.beginTransmission(Add);
 
      #for i in range (0,len):
      	bus.write_byte_data(address1,RainbowCMD[0-len]  #RainbowCMD[i]Wire.write(RainbowCMD[i]);
      									# Wire.endTransmission();    
      delay(5);   

}












def set_led(data,bank):
  if bank == 1:
   bus.write_byte_data(address,0x12,data)
  else:
   bus.write_byte_data(address,0x13,data)
  return

# Handle the command line arguments
def main():
   a = 0
delay = 0.05   
while True:

# Move led left  
   for x in range(0,8):
     a = 1 << x
     set_led(a,0)
     time.sleep(delay)
   set_led(0,0)
   for x in range(0,8):
     a = 1 << x
     set_led(a,1)
     time.sleep(delay)
   set_led(0,1)  
 
# Move led right 
   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,1)
     time.sleep(delay)
   set_led(0,1)
 
   for x in range(7,-1,-1):
     a = 1 << x
     set_led(a,0)
     time.sleep(delay)
   set_led(0,0)
   
  
if __name__ == "__main__":
   main()
