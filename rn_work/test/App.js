import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, SafeAreaView } from "react-native";
import VacationWrite from './components/VacatationWrite';
import VacationList from './components/VacationList';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import Main from './components/Main';


//navigation container는 react의 react-router-dom과 같은 형태다
//그러고 난 뒤 navigate stack이라는 걸 또 설치해서 Stack navigator로 또 감싸야 함



const Stack = createNativeStackNavigator();


export default function App() {
  return (
    <NavigationContainer>
      <SafeAreaView style={styles.container}>
        <Stack.Navigator initialRouteName="Main">
          <Stack.Screen name="Main" component={Main}/>
          <Stack.Screen name="VacationWrite" component={VacationWrite} />
          <Stack.Screen name="VacationList" component={VacationList} />
        </Stack.Navigator>
      </SafeAreaView>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {    
    flex: 1,
    backgroundColor: '#fff', 
    justifyContent: 'center',
  },
});
