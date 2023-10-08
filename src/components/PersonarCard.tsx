import styled from "styled-components";
import { PersonasData } from "../types";

const PersonaCardDiv = styled.div`
  width: 20em;
  border: 1px solid black;
  margin: 2em;
`;

interface Props {
  key: number;
  postProps: PersonasData;
}

const PersonarCard = ({ postProps }: Props) => {
  const headshot_url =
    import.meta.env.VITE_API_PATH +
    "/headshots/images/" +
    postProps["headshot_file"];
  return (
    <PersonaCardDiv className="card">
      <img className="card-img-top" src={headshot_url} />
      <div className="card-body">
        <p>Location: {postProps["ltla_name"]}</p>
        <p>Gender: {postProps["sex"]}</p>
        <p>Age: {postProps["age_category"]}</p>
        <p>Ethnicity: {postProps["ethnicity"]}</p>
        <p>Percentage of this demographic: {postProps["notes"]}</p>
        <p>Employment: {postProps["employment"]}</p>
      </div>
    </PersonaCardDiv>
  );
};

export default PersonarCard;
