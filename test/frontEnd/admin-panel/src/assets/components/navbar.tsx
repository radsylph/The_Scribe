import logo from "../../assets/react.svg";

function Navbar() {
  const btns = [
    {
      text: "btn1",
      link: "/link1",
    },
    {
      text: "btn2",
      link: "/link2",
    },
    {
      text: "btn3",
      link: "/link3",
    },
    {
      text: "btn4",
      link: "/link3",
    },
    {
      text: "btn5",
      link: "/link3",
    },
  ];

  return (
    <div className="bg-stone-100 flex-grow flex justify-center">
      <div className="m-2 p-1 self-center">
        <img src={logo} height={"55vh"} width={"45vw"} />
      </div>
      <div className="border-2 border-red-800 flex flex-grow justify-around">
        {btns.map((btn) => {
          return (
            <button className="bg-green-600 p-2 m-2 rounded hover:bg-green-800">
              <a
                href={btn.link}
                className="text-stone-800 hover:text-stone-600 m-4 text-xl "
              >
                {btn.text}
              </a>
            </button>
          );
        })}
      </div>
      <div className="bg-green-600 p-2 m-2 rounded hover:bg-green-800">
        options
      </div>
    </div>
  );
}

export default Navbar;
