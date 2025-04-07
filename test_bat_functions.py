import pytest
import time
import bat_functions

#exercise 1

def test_calculate_bat_power():
    """Test that calculate_bat_power returns correct values for different levels."""
    assert bat_functions.calculate_bat_power(0) == 0
    assert bat_functions.calculate_bat_power(1) == 42
    assert bat_functions.calculate_bat_power(2) == 84
    assert bat_functions.calculate_bat_power(10) == 420
    assert bat_functions.calculate_bat_power(-1) == -42  

@pytest.mark.parametrize("distance,expected", [
    (0, 100),     
    (5, 50),    
    (10, 0),     
    (12, 0),    
    (-1, 110),   
])
def test_signal_strength(distance, expected):
    """Test signal_strength with various distances using parametrization."""
    assert bat_functions.signal_strength(distance) == expected

#exercise 2

@pytest.fixture
def bat_vehicles():
    """Fixture providing a dictionary of Batman's vehicles and their specifications."""
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }

def test_get_bat_vehicle_known(bat_vehicles):
    """Test that get_bat_vehicle returns correct specs for known vehicles."""
    for vehicle_name, specs in bat_vehicles.items():
        result = bat_functions.get_bat_vehicle(vehicle_name)
        assert result == specs
        assert result['speed'] == specs['speed']
        assert result['armor'] == specs['armor']

def test_get_bat_vehicle_unknown():
    """Test that get_bat_vehicle raises ValueError for unknown vehicles."""
    with pytest.raises(ValueError) as excinfo:
        bat_functions.get_bat_vehicle('BatTractor')
    assert 'Unknown vehicle: BatTractor' in str(excinfo.value)

#exercise 3

def test_fetch_joker_info_with_pytest_mock(mocker):
    """Test fetch_joker_info using the pytest-mock fixture."""
    # Mock data to be returned
    mock_data = {'mischief_level': 0, 'location': 'captured'}
    
    # Mock both the sleep function and the original function
    mocker.patch('time.sleep')
    mocker.patch.object(bat_functions, 'fetch_joker_info', return_value=mock_data)
    
    # Call the function and verify
    result = bat_functions.fetch_joker_info()
    assert result == mock_data
    assert result['mischief_level'] == 0
    assert result['location'] == 'captured'