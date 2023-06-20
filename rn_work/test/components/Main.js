import { Button, View, StyleSheet, Image } from "react-native";
import calender from '../assets/images/calender.png'


const Main = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Button
        style={styles.mybtn}
        onPress={() => {
          navigation.navigate("VacationWrite");
        }}
        title="휴가계작성"
      ></Button>
      <Button
        style={styles.mybtn}
        onPress={() => {
          navigation.navigate("VacationList");
        }}
        title="휴가계목록"
      ></Button>
     
    </View>
  );
};

export default Main;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    justifyContent: "center",
    alignItems: "center",
  },
  mybtn: {
    // width:100,
    // margin:5
  },
});
