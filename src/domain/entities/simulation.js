const mongoose = require('mongoose');

const SimulationSchema = new mongoose.Schema({
    type: { type: String, required: true, enum: ['tension', 'projectile'] },
    data: {
        // Tension solver data
        weight: { type: Number },
        theta1: { type: Number },
        theta2: { type: Number },
        tension1: { type: Number },
        tension2: { type: Number },

        // Projectile motion data
        initialVelocity: { type: Number },
        angle: { type: Number },
        flightTime: { type: Number },
        maxHeight: { type: Number },
        range: { type: Number }
    },
    createdAt: { type: Date, default: Date.now },
});

module.exports = mongoose.model('Simulation', SimulationSchema);