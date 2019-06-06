import sys
sys.path.insert(0, '../')
import cozir

# Setting Up Cozir
co2Sensor = cozir.Cozir()

# For now just stable in polling mode
if(co2Sensor.opMode(co2Sensor.polling)):
    print("Cozir: Set Mode = K{0}".format(co2Sensor.act_OpMode))
    
hum = co2Sensor.humidity()
print("Humidity = "+ str(hum) + " %")