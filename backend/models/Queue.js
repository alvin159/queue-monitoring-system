const mongoose = require("mongoose");

const QueueSchema = new mongoose.Schema({
  id: { type: String, required: true },
  timestamp: { type: Date, default: Date.now },
  company_id: { type: String, required: true },
  store_id: { type: String, required: true },
  queue_length: { type: Number, required: true },
  confidence: { type: Number, required: true }
});

module.exports = mongoose.model("Queue", QueueSchema);
