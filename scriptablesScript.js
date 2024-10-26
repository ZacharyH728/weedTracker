// This script fetches data from a specified URL and displays it in a widget

// URL to fetch data from
const url = "http://1 00.113.211.33:8000/getOldestPurchase";

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
    let tmp = 0;
    data.forEach(item  => {
      tmp += item.amount
    })
    const amount = tmp 
    const date = new Date(data[0].date * 1000) || "No date";
    widget.addText(`Amount: ${amount}`);
    widget.addText(`Date: ${date.toLocaleString()}`);
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

