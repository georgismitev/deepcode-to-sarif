import json
import unittest
from deepcode_to_sarif import DeepCodeToSarif

class TestDeepCodeToSarif(unittest.TestCase):
  def test_critical_with_path(self):
    self.compare_files("tests/input-1.json", "tests/output-1.json")

  def test_warning_with_path(self):
    self.compare_files("tests/input-2.json", "tests/output-2.json")

  def test_critical_no_path(self):
    self.compare_files("tests/input-3.json", "tests/output-3.json")

  def test_no_issues(self):
    self.compare_files("tests/input-4.json", "tests/output-4.json")

  def test_issue_with_one_marker(self):
    self.compare_files("tests/input-5.json", "tests/output-5.json")

  def test_issue_with_no_markers(self):
    self.compare_files("tests/input-6.json", "tests/output-6.json")

  def compare_files(self, input_file_name, output_file_name):
    dc_input = None
    sarif_output = None

    with open(input_file_name) as input_json:
      dc_input = json.load(input_json)

    with open(output_file_name) as output_json:
      sarif_output = json.load(output_json)

    deepcode_sarif = DeepCodeToSarif(dc_input).convert_to_sarif()
    self.assertEqual(deepcode_sarif, sarif_output)

if __name__ == '__main__':
  unittest.main()