import multiprocessing
import argparse 

from pypi.src.slowblood import extract_text_from_pdf 

## MAIN
def main():

  ## PROCESS ARGS and PARAMETERS
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', type=str, help='i target_file.pdf')
  parser.add_argument('-o', type=str, help='o output_file.txt')
  args = parser.parse_args()
  print(args)

  ## Default if no -i input argument is set
  target_pdf_file = "ign/data/mock_invoice.pdf"
  if args.i != None:
    target_pdf_file = args.i

  print("===== Using PDF file:")
  print(target_pdf_file)

  content = extract_text_from_pdf(target_pdf_file)
  print(content)
  print("================================")

  if args.o != None:
    f = open(args.o, "w")
    f.write(content)
    f.close()

if __name__ == '__main__':
  multiprocessing.freeze_support()
  main()
