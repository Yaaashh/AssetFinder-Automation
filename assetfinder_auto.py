import subprocess
import argparse
import time
import os

def run_assetfinder(domain, output_file, subs_only=False):
    """Runs assetfinder for the specified domain and saves the output to a file.

    Args:
        domain (str): The target domain.
        output_file (str): The output file path.
        subs_only (bool): Output only subdomains if True.
    """

    # Construct the command
    command = ["assetfinder"]
    if subs_only:
        command.append("--subs-only")
    command.append(domain)

    try:
        # Run the assetfinder command
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Assetfinder completed successfully. Output saved to {output_file}")
            with open(output_file, "w") as f:
                f.write(result.stdout)
        else:
            print(f"Assetfinder failed with return code {result.returncode}")
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Automate Assetfinder with various options.")
    parser.add_argument("domain", help="The target domain")
    parser.add_argument("-o", "--output", default=None, help="Output file path")
    parser.add_argument("-subs", "--subs_only", action="store_true", help="Output only subdomains")

    args = parser.parse_args()

    # Define the output directory
    output_dir = "Assetfinder Output"
    
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate a default output file name if not provided
    if args.output is None:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        args.output = os.path.join(output_dir, f"{args.domain}_assetfinder_{timestamp}.txt")
    else:
        # If an output file is provided, place it in the specified directory
        args.output = os.path.join(output_dir, args.output)

    run_assetfinder(args.domain, args.output, args.subs_only)

if __name__ == "__main__":
    main()
