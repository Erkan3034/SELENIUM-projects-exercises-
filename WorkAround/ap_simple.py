from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def create_stealth_driver():
    """Create a Chrome driver that's harder to detect"""
    options = Options()
    
    # Stealth options
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    # Add realistic user agent
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Disable images to load faster
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    
    driver = webdriver.Chrome(options=options)
    
    # Remove webdriver property
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

def search_without_recaptcha():
    """Search using DuckDuckGo (usually no reCAPTCHA)"""
    print("Using DuckDuckGo to avoid reCAPTCHA...")
    
    driver = create_stealth_driver()
    
    try:
        # Go to DuckDuckGo
        driver.get("https://duckduckgo.com")
        time.sleep(2)
        
        # Find search box
        search_box = driver.find_element(By.NAME, "q")
        
        # Type search query
        search_box.send_keys("Selenium Python Nedir")
        time.sleep(1)
        
        # Press Enter
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # Get results
        results = driver.find_elements(By.XPATH, "//h2[@class='result__title'] | //a[@class='result__title']")
        
        print("\nDuckDuckGo Results:")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

def search_with_bing():
    """Search using Bing (less likely to have reCAPTCHA)"""
    print("Using Bing as alternative...")
    
    driver = create_stealth_driver()
    
    try:
        # Go to Bing
        driver.get("https://www.bing.com")
        time.sleep(2)
        
        # Find search box
        search_box = driver.find_element(By.NAME, "q")
        
        # Type search query
        search_box.send_keys("Selenium Python Nedir")
        time.sleep(1)
        
        # Press Enter
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        
        # Get results
        results = driver.find_elements(By.XPATH, "//h2 | //a[@class='title']")
        
        print("\nBing Results:")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

def main():
    """Main function - try different search engines"""
    print("Starting search automation...")
    
    # Try DuckDuckGo first (usually no reCAPTCHA)
    search_without_recaptcha()
    
    print("\n" + "="*50 + "\n")
    
    # Try Bing as backup
    search_with_bing()

if __name__ == "__main__":
    main() 