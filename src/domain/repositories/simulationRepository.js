const Simulation = require('../entities/simulation');

class SimulationRepository {
    async saveSimulation(data) {
        const simulation = new Simulation(data);
        return await simulation.save();
    }

    async getAllSimulations() {
        return await Simulation.find().sort({ createdAt: -1 });
    }

    async getSimulationById(id) {
        return await Simulation.findById(id);
    }

    async getSimulationsByType(type) {
        return await Simulation.find({ type }).sort({ createdAt: -1 });
    }
}

module.exports = new SimulationRepository();