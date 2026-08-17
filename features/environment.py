import allure
from utilities.driver_factory import DriverFactory

def before_scenario(context, scenario):
    context.driver = DriverFactory.get_driver("chrome")
    context.driver.maximize_window()

def after_scenario(context, scenario):
    # time.sleep(3)
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()

def after_step(context, step):
    if step.status == "failed":
        # Capture screenshot as a binary PNG stream
        screenshot = context.driver.get_screenshot_as_png()

        # Attach the binary stream directly to the Allure report
        allure.attach(
            screenshot,
            name=f"Failed: {step.name}",
            attachment_type=allure.attachment_type.PNG
        )

