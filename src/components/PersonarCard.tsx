import { PostData } from "../types";
import styled from "styled-components";

const PersonaCardDiv = styled.div`
  width: 20em;

  border: 1px solid black;
  margin: 2em;
`;

interface Props {
  key: number;
  postProps: PostData;
}

const PersonarCard = ({ key, postProps }: Props) => {
  const ethnicity = postProps["ethniticty"];
  const gender = postProps["Gender"];
  const age = postProps["age"];
  let gender_code = 0;

  let ethnicity_code = "other";
  if (ethnicity.includes("White")) {
    ethnicity_code = "white";
  } else if (ethnicity.includes("Black")) {
    ethnicity_code = "black";
  } else if (
    ethnicity.includes("Indian") ||
    ethnicity.includes("Pakistani") ||
    ethnicity.includes("Bangladeshi")
  ) {
    ethnicity_code = "indian";
  } else if (ethnicity.includes("Asian")) {
    ethnicity_code = "asian";
  }

  const query_string =
    "?age=" + age + "&gender=" + gender + "&ethnicity=" + ethnicity_code;
  const url = "http://127.0.0.1:105/image/headshot.jpg" + query_string;
  return (
    <PersonaCardDiv>
      <img className="headshot" src={url} />
      <p>Location: {postProps["LAname"]}</p>
      <p>Gender: {postProps["Gender"]}</p>
      <p>Age: {postProps["age"]}</p>
      <p>Ethnicity: {postProps["ethniticty"]}</p>
    </PersonaCardDiv>
  );
};

export default PersonarCard;
