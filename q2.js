function exercise2(breed, height, weight, male) {
    var Bulldog, Dalmatian, M;
    Bulldog = [15, 50, 14, 40];
    Dalmatian = [24, 70, 19, 45];
    M = [9, 7, 7, 6];
  
    if (breed === "Bulldog") {
      if (male === true) {
        if (height > Bulldog[0] - Bulldog[0] * 0.1 && height < Bulldog[0] + Bulldog[0] * 0.1) {
          if (weight > Bulldog[1] - Bulldog[1] * 0.1 && weight < Bulldog[1] + Bulldog[1] * 0.1) {
            return "True";
          } else {
            return "False";
          }
        } else {
          return "False";
        }
      } else {
        if (height > Bulldog[2] - Bulldog[2] * 0.1 && height < Bulldog[2] + Bulldog[2] * 0.1) {
          if (weight > Bulldog[3] - Bulldog[3] * 0.1 && weight < Bulldog[3] + Bulldog[3] * 0.1) {
            return "True";
          } else {
            return "False";
          }
        } else {
          return "False";
        }
      }
    } else {
      if (breed === "Dalmatian") {
        if (male === true) {
          if (height > Dalmatian[0] - Dalmatian[0] * 0.1 && height < Dalmatian[0] + Dalmatian[0] * 0.1) {
            if (weight > Dalmatian[1] - Dalmatian[1] * 0.1 && weight < Dalmatian[1] + Dalmatian[1] * 0.1) {
              return "True";
            } else {
              return "False";
            }
          } else {
            return "False";
          }
        } else {
          if (height > Dalmatian[2] - Dalmatian[2] * 0.1 && height < Dalmatian[2] + Dalmatian[2] * 0.1) {
            if (weight > Dalmatian[3] - Dalmatian[3] * 0.1 && weight < Dalmatian[3] + Dalmatian[3] * 0.1) {
              return "True";
            } else {
              return "False";
            }
          } else {
            return "False";
          }
        }
      } else {
        if (male === true) {
          if (height > M[0] - M[0] * 0.1 && height < M[0] + M[0] * 0.1) {
            if (weight > M[1] - M[1] * 0.1 && weight < M[1] + M[1] * 0.1) {
              return "True";
            } else {
              return "False";
            }
          } else {
            return "False";
          }
        } else {
          if (height > M[2] - M[2] * 0.1 && height < M[2] + M[2] * 0.1) {
            if (weight > M[3] - M[3] * 0.1 && weight < M[3] + M[3] * 0.1) {
              return "True";
            } else {
              return "False";
            }
          } else {
            return "False";
          }
        }
      }
    }
  }
  