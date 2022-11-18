package main

    import (
        "encoding/json"
        "fmt"
        "requests"
        )

var metadata_url;
metadata_url = "http://169.254.169.254/latest/meta-data/ami-id";

function expand_json(url) {
  var list_of_values, output, r, text;
  output = {};
  r = requests.get(metadata_url);
  text = r.text;
  list_of_values = r.text.splitlines();
  return list_of_values;
}

function get_metadata() {
  var result;
  result = expand_json(metadata_url);
  return result;
}

function get_metadata_json() {
  var metadata, metadata_json;
  metadata = get_metadata();
  metadata_json = json.dumps(metadata, {
    "indent": 4,
    "sort_keys": true
  });
  return metadata_json;
}

func main() {
  console.log(get_metadata_json());
}
