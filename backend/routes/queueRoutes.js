const express = require("express");
const Queue = require("../models/Queue");
const router = express.Router();

// Create a queue entry
router.post("/", async (req, res) => {
  try {
    const queue = new Queue(req.body);
    await queue.save();
    console.log("Queue created:", queue);
    res.status(201).json(queue);
  } catch (error) {
    console.error("Error creating queue:", error);
    res.status(500).json({ error: error.message });
  }
});

// Get all queue data
router.get("/", async (req, res) => {
  try {
    const queues = await Queue.find();
    console.log("All Queues:", queues);
    res.json(queues);
  } catch (error) {
    console.error("Error retrieving queues:", error);
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
