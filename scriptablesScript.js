// This script fetches data from a specified URL and displays it in a widget

// URL to fetch data from
const url = "http://100.75.225.103:5000/getLatestPurchase";

// Function to fetch data
async function fetchData() {
  try {
    const request = new Request(url);
    const response = await request.loadJSON();
    return response;
  } catch (error) {
    console.error("Error fetching data: ", error);
    return null;
  }
}

// Function to create the widget
async function createWidget(data) {
  const widget = new ListWidget();
  
  if (data) {
    // Assuming the JSON response has 'item', 'price', and 'date' keys
    const item = data.item || "No item";
    const price = data.price || "No price";
    const date = data.date || "No date";

    widget.addText(`Item: ${item}`);
    widget.addText(`Price: ${price}`);
    widget.addText(`Date: ${date}`);
  } else {
    widget.addText("Failed to load data");
  }

  return widget;
}

// Main function to run the script
async function run() {
  const data = await fetchData();
  const widget = await createWidget(data);
  if (config.runsInWidget) {
    Script.setWidget(widget);
  } else {
    widget.presentMedium();
  }
  Script.complete();
}

// Execute the script
await run();

