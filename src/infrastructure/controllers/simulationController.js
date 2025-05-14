const simulationUseCase = require('../../application/simulationUseCase');

exports.saveSimulation = async (req, res) => {
    try {
        const simulation = await simulationUseCase.createSimulation(req.body);
        res.status(201).json(simulation);
    } catch (error) {
        res.status(500).json({ message: 'Error guardando la simulación', error: error.message });
    }
};

exports.getSimulations = async (req, res) => {
    try {
        const { type } = req.query;
        const simulations = type
            ? await simulationUseCase.listSimulationsByType(type)
            : await simulationUseCase.listSimulations();
        res.status(200).json(simulations);
    } catch (error) {
        res.status(500).json({ message: 'Error obteniendo las simulaciones', error: error.message });
    }
};

exports.getSimulationById = async (req, res) => {
    try {
        const simulation = await simulationUseCase.getSimulation(req.params.id);
        if (!simulation) {
            return res.status(404).json({ message: 'Simulación no encontrada' });
        }
        res.status(200).json(simulation);
    } catch (error) {
        res.status(500).json({ message: 'Error obteniendo la simulación', error: error.message });
    }
};