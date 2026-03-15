```json
{
    "data/data_preprocessing.py": {
        "content": "
import logging
from typing import List, Dict
from ray import tune
from giskard import MemoryStore
from zapier_agent import LangGraph

logging.basicConfig(level=logging.INFO)

def non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for a given dataset.

    Args:
    - data (List[float]): A list of floating point numbers.

    Returns:
    - float: The non-stationary drift index.
    """
    try:
        # Calculate the mean and standard deviation of the data
        mean = sum(data) / len(data)
        std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
        # Calculate the non-stationary drift index
        drift_index = std_dev / mean
        return drift_index
    except ZeroDivisionError:
        logging.error('Cannot calculate drift index for zero mean')
        return None

def stochastic_regime_switch(data: List[float], threshold: float) -> List[float]:
    """
    Apply stochastic regime switch to a given dataset.

    Args:
    - data (List[float]): A list of floating point numbers.
    - threshold (float): The threshold for regime switching.

    Returns:
    - List[float]: The dataset after applying stochastic regime switch.
    """
    try:
        # Initialize an empty list to store the result
        result = []
        # Iterate over the data
        for x in data:
            # Apply stochastic regime switch
            if x > threshold:
                result.append(x * 2)
            else:
                result.append(x / 2)
        return result
    except Exception as e:
        logging.error(f'Error applying stochastic regime switch: {e}')
        return None

def graph_based_memory_management(graph: LangGraph) -> None:
    """
    Perform graph-based memory management using LangGraph.

    Args:
    - graph (LangGraph): A LangGraph object.
    """
    try:
        # Create a memory store
        memory_store = MemoryStore()
        # Add nodes and edges to the graph
        graph.add_node('node1')
        graph.add_node('node2')
        graph.add_edge('node1', 'node2')
        # Save the graph to the memory store
        memory_store.save_graph(graph)
    except Exception as e:
        logging.error(f'Error performing graph-based memory management: {e}')

def rocket_science_simulation() -> None:
    """
    Simulate the 'Rocket Science' problem.
    """
    try:
        # Initialize the data
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        # Calculate the non-stationary drift index
        drift_index = non_stationary_drift_index(data)
        logging.info(f'Non-stationary drift index: {drift_index}')
        # Apply stochastic regime switch
        switched_data = stochastic_regime_switch(data, 3.0)
        logging.info(f'Switched data: {switched_data}')
        # Perform graph-based memory management
        graph = LangGraph()
        graph_based_memory_management(graph)
    except Exception as e:
        logging.error(f'Error simulating rocket science: {e}')

if __name__ == '__main__':
    rocket_science_simulation()
",
        "commit_message": "feat: implement specialized data_preprocessing logic"
    }
}
```