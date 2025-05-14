const simulationRepository = require('../domain/repositories/simulationRepository');

class SimulationUseCase {
    async createSimulation(data) {
        return await simulationRepository.saveSimulation(data);
    }

    async listSimulations() {
        return await simulationRepository.getAllSimulations();
    }

    async listSimulationsByType(type) {
        return await simulationRepository.getSimulationsByType(type);
    }

    async getSimulation(id) {
        return await simulationRepository.getSimulationById(id);
    }
}

module.exports = new SimulationUseCase();