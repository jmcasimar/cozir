import sys
sys.path.insert(0, '../')
import cozir

# Setting Up Cozir
co2Sensor = cozir.Cozir()

# For now just stable in polling mode
if(co2Sensor.opMode(co2Sensor.polling)):
    print("Cozir: Set Mode = K{0}".format(co2Sensor.act_OpMode))
    
co2_filter = co2Sensor.co2() # Use filter
co2 = co2Sensor.co2(1) # Without filter
print("CO2 (smoothed) = "+ str(co2_filter) + " ppm")
print("CO2 = "+ str(co2) + " ppm")