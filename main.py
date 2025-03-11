from package import Package
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Test a standard package (small and light)
    logging.info("Test 1: Small and light package")
    result = Package(10, 20, 30, 5).sort()
    logging.info(f"Dimensions: 10x20x30 cm, Mass: 5 kg, Classification: {result}")

    # Test a special package (bulky but not heavy)
    logging.info("Test 2: Bulky but not heavy package")
    result = Package(100, 100, 100, 15).sort()
    logging.info(f"Dimensions: 100x100x100 cm, Mass: 15 kg, Classification: {result}")

    # Test a special package (not bulky but heavy)
    logging.info("Test 3: Not bulky but heavy package")
    result = Package(30, 40, 50, 25).sort()
    logging.info(f"Dimensions: 30x40x50 cm, Mass: 25 kg, Classification: {result}")

    # Test a rejected package (bulky and heavy)
    logging.info("Test 4: Bulky and heavy package")
    result = Package(150, 150, 150, 30).sort()
    logging.info(f"Dimensions: 150x150x150 cm, Mass: 30 kg, Classification: {result}")

    # Test a negative dimension package
    logging.info("Test 5: Negative dimension package")
    try:
        result = Package(-10, 20, 30, 5).sort()
        logging.info(f"Dimensions: -10x20x30 cm, Mass: 5 kg, Classification: {result}")
    except ValueError as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
