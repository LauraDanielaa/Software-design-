## Workshop 2
Using the code of workshop 1 in which we had to create a catalog of cars where we had to create engines with certain characteristics in this Workshop 2 we are going to make a catalog but in an updated form, changing some requirements as follows 
1. The cars must have the following attributes: transmission, chassis, year, make, model, fuel type and engine. 
2. Yachts must have the following attributes: length, weight, year, make, model and engine. 
3. Trucks and motorcycles shall keep the same attributes as before. However, only for trucks it is necessary to calculate the gasoline consumption due to US and European regulations. 
4. You need to add the following vehicle options, and you need to define the appropriate attributes they need: Helicopter, Scooter. 
5. Creating engines on the platform is not a good idea due to possible human errors. Therefore, it is a better idea to have some predefined engines for each of the vehicle types, dividing them into gas and electric engines. In addition, for each vehicle you should define low-end and high-end engines.
6. All engines should have the following attributes: stability, power, weight, dimensions, torque and maximum speed. 
7. You should reduce memory as much as possible, so check where you could reduce the creation of duplicate objects to avoid this. Be careful with memory references.

For this work in order to do it in an optimal way we intend to use the singleton creative design pattern, since it avoids that more than one object is created per class. 
