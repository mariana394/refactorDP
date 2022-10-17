# Patron de diseño: Simple Factory
from patterns.csv_utils import Ride

class TxtReport:
    def __init__(self, rides) -> None:
        self.rides = rides
        self.report = None

    def create_content(self):
        builder = [self._create_headers("Taxi Report"), self._create_table_headers()]
        for ride in self.rides:
            builder.append(self._add_ride(ride))
        self.report = "".join(builder)
        return "".join(builder)


    def create_file(self):
        with open("financial-report.txt", "w") as file:
            file.write(self.report)


    def _create_headers(self,title: str):
        return f"{title}\n\n"


    def _create_table_headers(self):
        return "".join([
            '\n',
            f"TaxiID\t",
            f"Pickup time\t\t",
            f"Dropoff time\t",
            f"\tPassenger count\t",
            f"Trip Distance\t",
            f"Total amount\t",
            "\n"
        ])

    def _add_ride(self,ride):
        return "".join([
            '\n',
            f"{ride.taxi_id}\t",
            f"{ride.pick_up_time.isoformat()}\t",
            f"{ride.drop_of_time.isoformat()}\t",
            f"{ride.passenger_count}\t",
            f"\t{ride.trip_distance}\t",
            f"\t{self._format_amount(ride.tolls_amount)}\t",
            "\n"
        ])


    def _format_amount(self,amount):
        if amount < 0:
            return f"({amount})"
        return str(amount)

class HtmlReport:
    def __init__(self, rides) -> None:
        self.rides = rides
        self.report = None
    
    def create_content(self):
        builder = [self._create_headers("Taxi Report"), self._create_table_headers()]
        for ride in self.rides:
            builder.append(self._add_ride(ride))
        builder.append(self._close_table_headers())
        self.report = "".join(builder)
        return "".join(builder)

    def create_file(self):
        with open("financial-report.html", "w") as file:
            file.write(self.report)

    def _create_headers(self,title: str):
        return f"<h1>{title}</h1>"

    def _create_table_headers(self):
        return """
        <table>
            <tr>
                <th> TaxiID </th>
                <th> Pickup time </th>
                <th> Dropoff time </th>
                <th> Passenger count </th>
                <th> Trip Distance </th>
                <th> Total amount </th>
            </tr>
        """

    def _close_table_headers(self):
        return "</table>"

    def _add_ride(self, ride):
        return "".join([
            "<tr>",
            f"<td>{ride.taxi_id}</td>",
            f"<td>{ride.pick_up_time.isoformat()}</td>",
            f"<td>{ride.drop_of_time.isoformat()}</td>",
            f"<td>{ride.passenger_count}</td>",
            f"<td>{ride.trip_distance}</td>",
            f"<td>{self._format_amount(ride.tolls_amount)}</td>",
            "</tr>"
        ])

    def _format_amount(self,amount):
        if amount < 0:
            return f"<span style='color:red'>{amount}</span>"
        return str(amount)

def get_report(report_type: str, rides):
    if report_type == "html":
        return HtmlReport(rides)
    elif report_type == "txt":
        return TxtReport(rides)
    else:
        raise Exception("Formato Desconocido")