import React, { useState } from "react";
import { Button, View, Image } from "react-native";
import DateTimePickerModal from "react-native-modal-datetime-picker";
import { AntDesign } from "@expo/vector-icons"; 

const DateCus = ({setStartdate,setEnddate,setBirthdate}) => {
  const [isDatePickerVisible, setDatePickerVisibility] = useState(false);

  const showDatePicker = () => {
    setDatePickerVisibility(true);
  };

  const hideDatePicker = () => {
    setDatePickerVisibility(false);
  };

  const handleConfirm = date => {
    console.warn("A date has been picked: ", date);
  
    try {
      const startdate = date.toLocaleString();
      const enddate = date.toLocaleString();
      const birthdate = date.toLocaleString();

      setStartdate && setStartdate(startdate.substring(0, 9));      
      setEnddate && setEnddate(enddate.substring(0, 9));
      setBirthdate && setBirthdate(birthdate.substring(0, 9));
    
      
    } catch (e) {
      console.log(e)
    }
    
    
    hideDatePicker();
  };

  return (
    <>
      {/* <Button title="Show Date Picker" onPress={showDatePicker} /> */}
      <AntDesign name="calendar" size={24} color="black" onPress={showDatePicker} />

      <DateTimePickerModal
        isVisible={isDatePickerVisible}
        mode="date"
        onConfirm={handleConfirm}
        onCancel={hideDatePicker}
      />
    </>
  );
};

export default DateCus;
