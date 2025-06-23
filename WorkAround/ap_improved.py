from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

def setup_driver():
    """Setup Chrome driver with anti-detection options"""
    chrome_options = Options()
    
    # Anti-detection options
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    
    # User agent to look more human
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Window size
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    # Execute script to remove webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def human_like_typing(element, text):
    """Type text like a human with random delays"""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))

def handle_cookies(driver):
    """Handle cookie consent popups"""
    try:
        # Wait for cookie consent and accept
        wait = WebDriverWait(driver, 5)
        accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Accept') or contains(text(), 'Kabul') or contains(text(), 'Agree')]")))
        accept_button.click()
        time.sleep(2)
    except:
        print("No cookie consent found or already accepted")

def handle_recaptcha(driver):
    """Handle reCAPTCHA if it appears"""
    try:
        # Check if reCAPTCHA is present
        recaptcha_frame = driver.find_element(By.XPATH, "//iframe[contains(@src, 'recaptcha')]")
        if recaptcha_frame:
            print("reCAPTCHA detected! Please solve it manually.")
            print("You have 30 seconds to solve the reCAPTCHA...")
            
            # Switch to reCAPTCHA frame
            driver.switch_to.frame(recaptcha_frame)
            
            # Wait for manual solving
            time.sleep(30)
            
            # Switch back to main content
            driver.switch_to.default_content()
            
            # Try to submit
            try:
                submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
                submit_button.click()
            except:
                pass
                
    except:
        print("No reCAPTCHA detected or already solved")

def search_with_alternatives():
    """Try different search engines if Google fails"""
    search_engines = [
        "https://www.bing.com",
        "https://duckduckgo.com",
        "https://www.yahoo.com"
    ]
    
    for engine in search_engines:
        try:
            print(f"Trying {engine}...")
            driver = setup_driver()
            driver.get(engine)
            
            # Handle cookies
            handle_cookies(driver)
            
            # Find search box (different for each engine)
            if "bing" in engine:
                search_box = driver.find_element(By.NAME, "q")
            elif "duckduckgo" in engine:
                search_box = driver.find_element(By.NAME, "q")
            elif "yahoo" in engine:
                search_box = driver.find_element(By.NAME, "p")
            
            # Type search query
            human_like_typing(search_box, "Selenium Python Nedir")
            time.sleep(1)
            search_box.send_keys(Keys.RETURN)
            
            # Wait for results
            time.sleep(3)
            
            # Get results
            results = driver.find_elements(By.XPATH, "//h3 | //h2 | //a[contains(@class, 'title')]")
            print(f"\nResults from {engine}:")
            for i, result in enumerate(results[:5], 1):
                print(f"{i}. {result.text}")
            
            driver.quit()
            return True
            
        except Exception as e:
            print(f"Error with {engine}: {e}")
            driver.quit()
            continue
    
    return False

def main():
    """Main function with Google search and fallback"""
    print("Starting Selenium search automation...")
    
    try:
        # Try Google first
        driver = setup_driver()
        driver.get("https://www.google.com")
        
        # Handle cookies
        handle_cookies(driver)
        
        # Wait for page to load
        time.sleep(2)
        
        # Find search box
        search_box = driver.find_element(By.NAME, "q")
        
        # Type search query like a human
        human_like_typing(search_box, "Selenium Python Nedir")
        time.sleep(1)
        
        # Press Enter
        search_box.send_keys(Keys.RETURN)
        
        # Wait for results
        time.sleep(3)
        
        # Check for reCAPTCHA
        handle_recaptcha(driver)
        
        # Get results
        results = driver.find_elements(By.XPATH, "//h3")
        print("\nGoogle Results:")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
        
        driver.quit()
        
    except Exception as e:
        print(f"Error with Google: {e}")
        try:
            driver.quit()
        except:
            pass
        
        # Try alternative search engines
        print("\nTrying alternative search engines...")
        search_with_alternatives()

if __name__ == "__main__":
    main() 