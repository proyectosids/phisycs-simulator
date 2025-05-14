const express = require('express');
const router = express.Router();
const simulationController = require('../controllers/simulationController');

// Rutas para ambos tipos de simulaciones
router.post('/', simulationController.saveSimulation);
router.get('/', simulationController.getSimulations);
router.get('/:id', simulationController.getSimulationById);

module.exports = router;