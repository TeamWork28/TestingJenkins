#!/usr/bin/env python3
"""
Jenkins-compatible Python script example
This script demonstrates a basic Python program that is designed to run reliably in Jenkins.
"""

import os
import sys
import logging
import argparse
import traceback
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger('jenkins-script')

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Jenkins-compatible Python script')
    parser.add_argument('--input-dir', type=str, help='Input directory path', default='./input')
    parser.add_argument('--output-dir', type=str, help='Output directory path', default='./output')
    return parser.parse_args()

def check_environment():
    """Check if required environment variables are set."""
    required_vars = ['WORKSPACE']
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    
    if missing_vars:
        logger.warning(f"Missing environment variables: {', '.join(missing_vars)}")
        logger.info("Not a Jenkins environment or variables not set. Using defaults.")
    else:
        logger.info("Jenkins environment detected.")
    
    # Print environment information for debugging
    logger.info(f"Python version: {sys.version}")
    logger.info(f"Working directory: {os.getcwd()}")
    
    # Create a test file to verify write permissions
    try:
        with open('test_write.txt', 'w') as f:
            f.write('Test write')
        os.remove('test_write.txt')
        logger.info("Write permission confirmed")
    except Exception as e:
        logger.error(f"No write permission in current directory: {str(e)}")
        return False
    
    return True

def create_directories(input_dir, output_dir):
    """Create input and output directories if they don't exist."""
    try:
        os.makedirs(input_dir, exist_ok=True)
        logger.info(f"Input directory ensured: {input_dir}")
        
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Output directory ensured: {output_dir}")
        return True
    except Exception as e:
        logger.error(f"Failed to create directories: {str(e)}")
        return False

def main_process(input_dir, output_dir):
    """Main processing logic of the script."""
    try:
        # Simulate some work
        logger.info("Starting main process...")
        
        # This is where your actual processing would go
        # For this example, we'll just create a sample output file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"result_{timestamp}.txt")
        
        with open(output_file, 'w') as f:
            f.write(f"Process completed successfully at {datetime.now()}\n")
            f.write(f"Input directory: {input_dir}\n")
            f.write(f"Output directory: {output_dir}\n")
        
        logger.info(f"Created output file: {output_file}")
        logger.info("Main process completed successfully")
        return True
    except Exception as e:
        logger.error(f"Error in main process: {str(e)}")
        logger.error(traceback.format_exc())
        return False

def run():
    """Main execution function."""
    exit_code = 0
    start_time = datetime.now()
    logger.info(f"Script started at {start_time}")
    
    try:
        args = parse_arguments()
        
        if not check_environment():
            logger.error("Environment check failed")
            return 1
        
        if not create_directories(args.input_dir, args.output_dir):
            logger.error("Failed to create required directories")
            return 1
        
        if not main_process(args.input_dir, args.output_dir):
            logger.error("Main process failed")
            return 1
        
        logger.info("All tasks completed successfully")
    
    except Exception as e:
        logger.error(f"Unhandled exception: {str(e)}")
        logger.error(traceback.format_exc())
        exit_code = 1
    
    finally:
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        logger.info(f"Script ended at {end_time} (duration: {duration:.2f} seconds)")
        return exit_code

if __name__ == "__main__":
    sys.exit(run())