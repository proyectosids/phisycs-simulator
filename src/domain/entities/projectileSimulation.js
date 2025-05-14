const mongoose = require('mongoose');

const ProjectileSimulationSchema = new mongoose.Schema({
    initialVelocity: { type: Number, required: true },
    angle: { type: Number, required: true },
    flightTime: { type: Number, required: true },
    maxHeight: { type: Number, required: true },
    range: { type: Number, required: true },
    createdAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model('ProjectileSimulation', ProjectileSimulationSchema);