import time
import botbook_mcp3002 as mcp

smokeLevel = 0

def main():
        while True:
                smokeLevel = mcp.readAnalog()
                print("Current smoke level is %i " % smokeLevel)
                if smokeLevel > 120:
                        print("Smoke detected")
                        sendEmail("Smoke","Smoke level was %i" % smokeLevel)
                        time.sleep(gracePeriod)
                time.sleep(0.5)

if __name__ == "__main__":
        main()
